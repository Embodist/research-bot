# Skills & external source collections

## Skill format

A skill is a directory containing `SKILL.md` with YAML front-matter and a Markdown body — exactly the
[DeerFlow skill convention](https://github.com/bytedance/deer-flow/tree/main/skills/public):

```markdown
---
name: my-skill
description: One sentence. Describe WHEN to trigger, not just what it is.
---

# Body
Methodology, checklists, reference material …
```

`research_bot.skills.load_skills()` merges:

1. `<repo>/skills/*/SKILL.md` (local, wins on name conflict), then
2. `<repo>/deer-flow/skills/public/*/SKILL.md` (upstream submodule, optional).

The skills named in `research.skills` are injected into every planner / researcher / critic / synthesizer
system prompt.

## Skills shipped here

| Skill | Use |
| --- | --- |
| `deep-research` | the 4-phase methodology every run starts from |
| `frontier-tracking` | build a dated timeline; separate "new" from "validated" |
| `paper-survey` | paper graph, taxonomy, citation discipline |
| `evidence-grading` | A–E evidence levels, conflict resolution, wording rules |
| `embodied-ai` | simulators, benchmarks, method lineage |
| `vla` | architecture paradigms, model/dataset catalogue |
| `kinematics` | DH vs screw, IK methods, trajectory/whole-body control, libraries |
| `cpp-robotics` | Eigen/Sophus/Ceres/Pinocchio, real-time C++, build systems, pybind |
| `ros2` | distributions, DDS/RMW, executors, ros2_control/Nav2/MoveIt2, Zenoh |
| `dataset-hunting` | dataset/benchmark audit checklist |
| `report-writing` | report structure and citation format |

## Importing a skill

From the DeerFlow submodule (already available):

```bash
cp -r deer-flow/skills/public/systematic-literature-review skills/
rb skills show systematic-literature-review
```

From a URL (auto-handles `github.com` → `ghfast.top` mirror when needed):

```bash
scripts/import_skill.sh https://github.com/OWNER/REPO/blob/main/skills/foo/SKILL.md
scripts/import_skill.sh --name my-skill https://raw.githubusercontent.com/OWNER/REPO/main/SKILL.md
```

## Curated external collections (surveyed 2026-10)

These are the best-maintained collections found while building this bot. They are useful as **seed
catalogues** for new topics — not vendored wholesale.

### Agent / skill collections

| Collection | URL |
| --- | --- |
| VoltAgent/awesome-agent-skills | https://github.com/VoltAgent/awesome-agent-skills |
| travisvn/awesome-claude-skills | https://github.com/travisvn/awesome-claude-skills |
| sickn33/agentic-awesome-skills | https://github.com/sickn33/agentic-awesome-skills |
| lingxling/awesome-skills-cn | https://github.com/lingxling/awesome-skills-cn |
| bytedance/deer-flow skills (upstream) | https://github.com/bytedance/deer-flow/tree/main/skills/public |

### Robotics / embodied AI / VLA awesome-lists

| Collection | URL |
| --- | --- |
| Orlando-CS/Awesome-VLA | https://github.com/Orlando-CS/Awesome-VLA |
| yueen-ma/Awesome-VLA | https://github.com/yueen-ma/awesome-vla |
| DravenALG/awesome-vla-wam | https://github.com/DravenALG/awesome-vla-wam |
| wadeKeith/Awesome-Embodied-AI | https://github.com/wadeKeith/Awesome-Embodied-AI |
| GlimmerLab/Awesome-Embodied-AI-Robot | https://github.com/GlimmerLab/Awesome-Embodied-AI-Robot |
| fengtt42/Awesome-Autonomous-Embodied-AI-from-Scratch | https://github.com/fengtt42/Awesome-Autonomous-Embodied-AI-from-Scratch |
| RayYoh/Awesome-Robot-Learning | https://github.com/RayYoh/Awesome-Robot-Learning |
| YanjieZe/awesome-humanoid-robot-learning | https://github.com/YanjieZe/awesome-humanoid-robot-learning |
| BaiShuanghao/Awesome-Robotics-Manipulation | https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation |
| HaoranZhangumich/Awesome-Robotic-Benchmarks | https://github.com/HaoranZhangumich/Awesome-Robotic-Benchmarks |
| ziyaow1010/vla-datasets-benchmarks | https://github.com/ziyaow1010/vla-datasets-benchmarks |
| fkromer/awesome-ros2 | https://github.com/fkromer/awesome-ros2 |
| ahundt/awesome-robotics | https://github.com/ahundt/awesome-robotics |

To turn one into a research topic, copy a seed catalogue into `topics/<name>.yaml` under
`seed_resources:` and add `seed_queries/venues`.

## Adding a topic

```bash
cp topics/vla.yaml topics/my-topic.yaml
# edit: name, title, description, keywords, venues, seed_queries, seed_resources
rb topics show my-topic
rb run --topic my-topic --depth standard
```
