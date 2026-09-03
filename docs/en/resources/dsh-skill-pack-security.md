---
title: "dsh-skill-pack-security"
description: "Security-audit skill pack: 5 agent skills covering secret scan, dependency audit and more."
keywords: "dsh-skill-pack-security, security, skill, coding, deepseek harness, dsh"
---
# dsh-skill-pack-security

> ⭐ **2** · ✅ active · skill

| | | | |
|---|---|---|---|
| Type | skill | Category | Security |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | 2026-08-21 |

## One-liner

> Security-audit skill pack: 5 agent skills covering secret scan, dependency audit and more.

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-skill-pack-security` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Eight security-audit skills plus an automated plugin supply-chain gate for DeepSeek Harness.** *The skills teach the audit methodology; the `plugin_vet` tool executes the pre-install scan — license / SBOM / commit pinning / malicious patterns / five-dimension risk card.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-skill-pack-security` (counts toward the [deepseek1024.com](https://d

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-skill-pack-security#main"

# or from npm (published releases)
dsh plugin --profile web add @perrylink/dsh-skill-pack-security-provider

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A3 'id: skill-pack-security'
```

## 🚀 Quick Start

```bash
./scripts/install.ps1 -Target user-agents -Language zh   # Target: project-dsh | project-agents | user-dsh | user-agents; Language: zh (default) | en
```

## 📚 Learn more

**plugin_vet — the automated pre-install gate**

`plugin_vet` is the pack's automated complement: a zero-dependency scanner registered by the `provider/` plugin on `ctx.tools`. Point it at a GitHub `owner/repo` or a local package path — it downloads the tarball once (timeout + `AbortSignal` respected), scans within budget limits, and returns a render card. **Install gate.** The verdict feeds an installation gate — `gate.policy: warn` (default, n

**Installing the skills by hand**

DSH's local skill provider scans four roots by rank (lower rank wins same-name conflicts within a layer): Ranks (lower wins same-name conflicts within a layer): `project-dsh 100 < project-agents 200 < custom 300 < user-dsh 400 < user-agents 500`. Custom rank 300 is plugin-registered (such as this pack's optional `provider/`), not a disk root. ./scripts/install.ps1 -Target user-agents -Language zh 

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). `provider/cordis.patch.yml` documents each key inline.

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-skill-pack-security)
- [Full README](https://github.com/PerryLink/dsh-skill-pack-security#readme)
- [Back to the Skills list](../skills.md)
