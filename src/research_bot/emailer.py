"""Email delivery of the research report over SMTP (stdlib only)."""

from __future__ import annotations

import html as html_mod
import logging
import smtplib
import ssl
from email.message import EmailMessage
from pathlib import Path
from typing import Any

from .engine import ResearchResult
from .util import now_utc, truncate

log = logging.getLogger(__name__)


def _recipients(cfg: Any) -> list[str]:
    to = cfg.to
    if isinstance(to, str):
        to = [to]
    return [str(x).strip() for x in (to or []) if str(x).strip()]


def is_configured(cfg: Any) -> bool:
    return bool(cfg.smtp_host and cfg.username and cfg.password and cfg["from"] and _recipients(cfg))


def _markdown_to_html(md: str) -> str:
    """Very small Markdown → HTML for the email body (headings, lists, tables, code)."""
    lines = md.splitlines()
    out: list[str] = []
    in_ul = False
    in_table = False
    for line in lines:
        stripped = line.rstrip()
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if not in_table:
                out.append('<table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse">')
                in_table = True
                out.append("<tr>" + "".join(f"<th>{html_mod.escape(c)}</th>" for c in cells) + "</tr>")
            elif set(stripped.replace("|", "").replace(" ", "").replace("-", "").replace(":", "")) <= set():
                continue  # separator row
            else:
                out.append("<tr>" + "".join(f"<td>{html_mod.escape(c)}</td>" for c in cells) + "</tr>")
            continue
        if in_table:
            out.append("</table>")
            in_table = False
        if stripped.startswith("- ") or stripped.startswith("* "):
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{html_mod.escape(stripped[2:])}</li>")
            continue
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if stripped.startswith("# "):
            out.append(f"<h2>{html_mod.escape(stripped[2:])}</h2>")
        elif stripped.startswith("## "):
            out.append(f"<h3>{html_mod.escape(stripped[3:])}</h3>")
        elif stripped.startswith("### "):
            out.append(f"<h4>{html_mod.escape(stripped[4:])}</h4>")
        elif stripped.startswith(">"):
            out.append(f"<blockquote>{html_mod.escape(stripped.lstrip('> '))}</blockquote>")
        elif stripped:
            out.append(f"<p>{html_mod.escape(stripped)}</p>")
    if in_ul:
        out.append("</ul>")
    if in_table:
        out.append("</table>")
    return "\n".join(out)


def send_report(
    cfg: Any,
    result: ResearchResult,
    *,
    report_path: Path | None = None,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Send one report. Returns a delivery record (never raises)."""
    recipients = _recipients(cfg)
    record: dict[str, Any] = {
        "sent": False,
        "to": recipients,
        "ts": now_utc().replace(microsecond=0).isoformat(),
        "error": None,
        "dry_run": dry_run,
    }
    if not cfg.enabled and not dry_run:
        record["error"] = "email disabled"
        return record
    if not recipients:
        record["error"] = "no recipients configured"
        return record

    subject = f"{cfg.subject_prefix} {result.title} ({result.topic})"
    text_body = result.report_md
    if len(text_body) > 100_000:
        text_body = truncate(text_body, 100_000)

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = cfg["from"]
    msg["To"] = ", ".join(recipients)
    msg.set_content(text_body)
    msg.add_alternative(
        f"<html><body style='font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.6'>"
        f"<p><b>{html_mod.escape(result.title)}</b> · topic={html_mod.escape(result.topic)} · "
        f"depth={result.depth} · sources={len(result.references)}</p>"
        f"{_markdown_to_html(result.report_md)}</body></html>",
        subtype="html",
    )

    if cfg.attach_report and report_path and report_path.is_file():
        data = report_path.read_bytes()
        msg.add_attachment(data, maintype="text", subtype="markdown", filename=report_path.name)

    if dry_run or not is_configured(cfg):
        if not is_configured(cfg) and not dry_run:
            record["error"] = "smtp not fully configured"
            return record
        log.info("[dry-run] would send %r to %s", subject, recipients)
        record["sent"] = True
        record["dry_run"] = True
        return record

    try:
        port = int(cfg.smtp_port)
        if cfg.smtp_ssl:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(cfg.smtp_host, port, timeout=30, context=context) as server:
                server.login(cfg.username, cfg.password)
                server.send_message(msg, from_addr=cfg["from"], to_addrs=recipients)
        else:
            with smtplib.SMTP(cfg.smtp_host, port, timeout=30) as server:
                server.ehlo()
                server.starttls(context=ssl.create_default_context())
                server.login(cfg.username, cfg.password)
                server.send_message(msg, from_addr=cfg["from"], to_addrs=recipients)
        record["sent"] = True
        log.info("email sent to %s", recipients)
    except Exception as exc:  # noqa: BLE001
        record["error"] = str(exc)
        log.error("email delivery failed: %s", exc)
    return record


def send_digest(cfg: Any, results: list[ResearchResult], *, report_paths: list[Path] | None = None, dry_run: bool = False) -> dict[str, Any]:
    """Merge several reports into one digest email."""
    recipients = _recipients(cfg)
    record: dict[str, Any] = {
        "sent": False,
        "to": recipients,
        "ts": now_utc().replace(microsecond=0).isoformat(),
        "error": None,
        "dry_run": dry_run,
        "topics": [r.topic for r in results],
    }
    if not results:
        record["error"] = "no reports"
        return record
    if not cfg.enabled and not dry_run:
        record["error"] = "email disabled"
        return record
    if not recipients:
        record["error"] = "no recipients configured"
        return record

    subject = f"{cfg.subject_prefix} Daily digest — {len(results)} topic(s)"
    parts = [f"# {subject}", ""]
    for res in results:
        parts.append(f"\n\n---\n\n## {res.title} (`{res.topic}`)")
        parts.append(res.report_md)
    body = "\n".join(parts)

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = cfg["from"]
    msg["To"] = ", ".join(recipients)
    msg.set_content(body)
    msg.add_alternative(
        f"<html><body style='font-family:system-ui,sans-serif;line-height:1.6'>{_markdown_to_html(body)}</body></html>",
        subtype="html",
    )
    for path in report_paths or []:
        if path and path.is_file():
            msg.add_attachment(path.read_bytes(), maintype="text", subtype="markdown", filename=path.name)

    if dry_run or not is_configured(cfg):
        record["sent"] = bool(dry_run)
        if not dry_run:
            record["error"] = "smtp not fully configured"
        return record
    try:
        port = int(cfg.smtp_port)
        if cfg.smtp_ssl:
            with smtplib.SMTP_SSL(cfg.smtp_host, port, timeout=30, context=ssl.create_default_context()) as server:
                server.login(cfg.username, cfg.password)
                server.send_message(msg, from_addr=cfg["from"], to_addrs=recipients)
        else:
            with smtplib.SMTP(cfg.smtp_host, port, timeout=30) as server:
                server.ehlo()
                server.starttls(context=ssl.create_default_context())
                server.login(cfg.username, cfg.password)
                server.send_message(msg, from_addr=cfg["from"], to_addrs=recipients)
        record["sent"] = True
    except Exception as exc:  # noqa: BLE001
        record["error"] = str(exc)
    return record
