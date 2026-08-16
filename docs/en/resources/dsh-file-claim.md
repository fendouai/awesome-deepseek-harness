---
title: "dsh-file-claim"
description: "File ownership/claim system for parallel agent sessions on the same project: claim/release, heartbeat stale takeover and async 3-way merge."
keywords: "dsh-file-claim, developer, plugin, files, multi-agent, git, deepseek harness, dsh"
---
# dsh-file-claim

> ⭐ 3 · ✅ active · plugin

## One-liner

File ownership/claim system for parallel agent sessions on the same project: claim/release, heartbeat stale takeover and async 3-way merge.

## About

When several DSH sessions run in parallel against one workspace, they have no awareness of each other: two sessions can overwrite the same file, a crashed session leaves stale state behind, and a session that wants to edit a file another session owns can only wait or guess. `dsh-file-claim` turns a proven coordination protocol into native DSH tools, lifecycle events, and a write guard — so parallel agents cooperate instead of clobbering each other. claim_files({ paths: ["README.md"] }) # "I'm ed

## Author
**[Nwflower](https://github.com/Nwflower)**

## Links

- [GitHub Repository](https://github.com/Nwflower/dsh-file-claim)
- [Full README](https://github.com/Nwflower/dsh-file-claim#readme)
- [Back to the Plugins list](../plugins.md)
