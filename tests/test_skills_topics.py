from __future__ import annotations

from pathlib import Path

from research_bot.skills import load_skills, parse_skill_file, select_skills
from research_bot.topics import load_topics, resolve_topics

REPO = Path(__file__).resolve().parents[1]


def test_parse_skill_file(tmp_path):
    d = tmp_path / "myskill"
    d.mkdir()
    (d / "SKILL.md").write_text(
        "---\nname: myskill\ndescription: does things\n---\n\n# Body\ncontent here\n", encoding="utf-8"
    )
    skill = parse_skill_file(d / "SKILL.md")
    assert skill is not None
    assert skill.name == "myskill"
    assert skill.description == "does things"
    assert "content here" in skill.body


def test_parse_skill_file_no_frontmatter(tmp_path):
    d = tmp_path / "plain"
    d.mkdir()
    (d / "SKILL.md").write_text("# Just markdown\n", encoding="utf-8")
    skill = parse_skill_file(d / "SKILL.md")
    assert skill is not None
    assert skill.name == "plain"


def test_load_local_skills():
    skills = load_skills(REPO)
    for name in ("deep-research", "vla", "ros2", "kinematics", "cpp-robotics", "evidence-grading"):
        assert name in skills, name
        assert skills[name].source == "local"


def test_select_skills_ignores_unknown():
    skills = load_skills(REPO)
    got = select_skills(skills, ["vla", "does-not-exist"])
    assert [s.name for s in got] == ["vla"]


def test_skill_prompt_rendering():
    skills = load_skills(REPO)
    prompt = skills["deep-research"].to_prompt()
    assert "Skill: deep-research" in prompt
    assert len(prompt) > 100


def test_load_topics():
    topics = load_topics(REPO)
    for name in ("vla", "embodied-ai", "kinematics", "cpp-robotics", "ros2"):
        assert name in topics, name
    vla = topics["vla"]
    assert vla.seed_queries
    assert vla.seed_resources.get("papers")
    assert vla.seed_resources.get("datasets")


def test_resolve_topics():
    topics = load_topics(REPO)
    assert len(resolve_topics(topics, ["all"])) == len(topics)
    assert [t.name for t in resolve_topics(topics, ["vla"])] == ["vla"]
    assert resolve_topics(topics, ["nope"]) == []
