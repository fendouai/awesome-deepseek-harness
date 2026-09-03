---
title: "dsh-science"
description: "Reproducible Python and R work on DeepSeek Harness, built as plugins."
keywords: "dsh-science, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-science

> ⭐ **9** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 9 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | — |

## One-liner

> Reproducible Python and R work on DeepSeek Harness, built as plugins.

## About

--- **A Claude Science–style research workbench for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) — for genomics / pathogens / human health / bioinformatics projects.** - **ReAct research loop engine** — `research_init` / `research_state` / `research_hypothesis` / `research_experiment` / `research_findings` / `research_phase` / `research_review` / `research_report`, persisted in a `research-manifest.json` state machine (Question → Hypothesis → Experiment → Observe → Analyze → Conclude → Next Question). - **Versioned artifacts with provenance** — `artifact_save` / `artifact_list` / `artifact_show` / `artifact_diff` / `artifact_verify` / `artifact_deprecate` / `artifact_reproduce`: every result saved as `artifacts//v/` with per-file SHA-256, `artifact.json` provenance (

## ✨ Key Features

- **ReAct research loop engine** — `research_init` / `research_state` / `research_hypothesis` / `research_experiment` / `research_findings` / `research_phase` / `
- **Versioned artifacts with provenance** — `artifact_save` / `artifact_list` / `artifact_show` / `artifact_diff` / `artifact_verify` / `artifact_deprecate` / `ar
- **Remote compute engine (SSH / HPC clusters)** — 16 tools: `remote_host_add` / `remote_host_probe` / `remote_host_notes` / `remote_run` / `remote_status` / `rem
- **Remote Hosts config UI (bundle/profile-level)** — a Settings > 远程主机 page (the analog of Claude Science's Settings > Compute > SSH hosts): list/add/probe/edit/
- **Model Tier router (tiered, cross-provider)** — via the companion bundle [`dsh-model-tier`](packages/dsh-model-tier/): within one session, automatically routes
- **11 science skills** — research-loop, science-project-setup, artifact-provenance, scientific-reviewer, literature-connector, parallel-delegation, manuscript-wr

## 📦 Install

```bash
dsh plugin --profile web add dsh-science            # after npm publish
# or straight from GitHub:
dsh plugin --profile web add "github:biociao/dsh-science"
```

## 🚀 Quick Start

```bash
git clone https://github.com/biociao/dsh-science ~/.dsh/.agent-presets/science
# or from a local checkout:
bash scripts/install.sh          # copy   (or: bash scripts/install.sh link)
```

## 📚 Learn more

**Quick start (first session)**

1. `research_init` — create `research-manifest.json` + the project skeleton (`experiments/ literature/ artifacts/ analyses/ figures/ manuscript/ reviews/ data/ envs/`). 2. Read `research_state` at the start of every session; the loop state persists across sessions. 3. Run the loop: `research_hypothesis` (H1/H2/…) → `research_experiment` (E01/…, creates `experiments/<id>/{design.md,log.md,code/,res

**FAQ**

**Why subpath exports and not relative paths in the bundle?** `dsh plugin add` installs the package into the profile and its `cordis.patch.yml` rows join the profile composition. The profile loader resolves a row `name` relative to the **profile directory** (not the package), so `./engines/x.mjs` fails with `ERR_MODULE_NOT_FOUND`. Referencing `dsh-science/engines/x.mjs` (subpath export, `exports` 

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-science)
- [Full README](https://github.com/omdsh-dev/dsh-science#readme)
- [Back to the Plugins list](../plugins.md)
