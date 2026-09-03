---
title: "dsh-md-notes"
description: "A note-taking plugin for DeepSeek Harness (DSH). It provides a full MD notes manager and MD notes editor, letting you quickly capture conversation content into notes. Notes can be maintained by syncing to a Git repository"
keywords: "dsh-md-notes, ui, plugin, coding, git, deepseek harness, dsh"
---
# dsh-md-notes

> ⭐ **15** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 15 | Status | ✅ active |
| Author | [XieZongChen](https://github.com/XieZongChen) | Updated | — |

## One-liner

> A note-taking plugin for DeepSeek Harness (DSH). It provides a full MD notes manager and MD notes editor, letting you quickly capture conversation content into notes. Notes can be maintained by syncing to a Git repository

## About

A note-taking plugin for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH). It provides a full **MD notes manager** and **MD notes editor**, letting you quickly capture conversation content into notes. Notes can be maintained by syncing to a Git repository. **Who it's for**: DSH web users who want local, file-based notes (no database, no cloud) — capture a conversation into a note with one click, keep editing the `.md` anywhere, and back up / sync with a Git repository. **Current features**: - **Sidebar notes entry** → full-screen notes manager: per-workspace note list (grouped, collapsible), markdown edit/preview, save, delete (in-page confirm), create with one click. - **Assistant-message action** (next to copy) → pick or create a note and append that conversation

## ✨ Key Features

- **Sidebar notes entry** → full-screen notes manager: per-workspace note list (grouped, collapsible), markdown edit/preview, save, delete (in-page confirm), crea
- **Assistant-message action** (next to copy) → pick or create a note and append that conversation (user question + answer) to it **instantly** — the text is capt
- **Reference notes in chat (`@`)**: type `@` to pick notes (cross-workspace included); on send the host injects each note's content into the model context, so th
- **Git sync** (optional, URL-driven): **shared repo** mode (one repo for all workspaces, per-workspace folders) or **own repos** mode (per workspace: URL + branc
- **Note write mutex**: writes to the same note are locked across sessions — the sidebar entry, picker and manager stay in sync until the write finishes.
- **Settings panel** (dsh Settings → MD Notes): mode, repo URL/branch/subpath, auto-pull, commit author — with dsh-styled form controls.

## 📦 Install

```bash
dsh plugin --profile web add dsh-md-notes
```

## 🚀 Quick Start

```bash
dsh plugin --profile web update dsh-md-notes
```

## 📚 Learn more

**Install / Uninstall**

Prerequisites: `dsh` CLI installed, target profile is `web`. Install from npm (recommended): dsh plugin --profile web add dsh-md-notes Then **restart dsh web** (bundle layer and client package metadata are cached in the process; a restart is required for changes to take effect). Upgrade: dsh plugin --profile web update dsh-md-notes A restart of dsh web is required for it to take effect. Uninstall:

**Quick start**

1. Install the plugin (above), restart dsh web. 2. **Create a note**: click the notes entry at the bottom of the sidebar (above Settings) → click **+** on a workspace row → in the dialog enter a title (default "Untitled note <date>") and an optional **file name** → type in the editor → **Save**. 3. **Capture a conversation**: below any assistant answer, click the notes icon (next to copy) → pick a

**Configuration**

All options are plugin Config keys, overridable in the profile's `cordis.patch.yml` (a patch replaces the whole `config` of the row): config: route: '/plugins/md-notes' # HTTP API prefix; default is fine gitMode: 'off' # 'off' | 'shared' | 'own' gitAutoPull: true # pull remote before opening a note There are **no environment variables and no secrets** in this plugin's configuration.

## 🔗 Links

- [GitHub Repository](https://github.com/XieZongChen/dsh-md-notes)
- [Full README](https://github.com/XieZongChen/dsh-md-notes#readme)
- [Back to the Plugins list](../plugins.md)
