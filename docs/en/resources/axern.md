---
title: "Axern"
description: "Open-source sandboxes for AI agents: untrusted code execution and durable services."
keywords: "Axern, harness, related, security, deepseek harness, dsh"
---
# Axern

> ⭐ **57** · ✅ active · related · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | related | Category | Harness |
| Stars | ⭐ 57 | Status | ✅ active |
| Author | [cofy-x](https://github.com/cofy-x) | Updated | 2026-08-21 |

## One-liner

> Open-source sandboxes for AI agents: untrusted code execution and durable services.

## About

The supported local path runs the complete stack with Docker Compose. It needs only the `axern` CLI and Docker Compose v2 — no source checkout, Make, Helm, or language toolchains. brew install cofy-x/tap/axern Without Homebrew, use the standalone checksummed installer: curl -fsSL https://raw.githubusercontent.com/cofy-x/axern/main/install.sh | sh Then start Axern and run the first workload: axern local up axern local image load python:3.12-slim --pull axern run python:3.12-slim -- python -c 'print("hello from axern")' `local up` starts PostgreSQL, MinIO, the control and node services, waits for readiness, and creates the `local` context. `local image load` streams the selected host Docker image into that local node without a temporary archive: axern context current axern run list axern loc

## ✨ Key Features

- **Agent sandboxes:** execute agent-generated code behind a runsc isolation boundary while retaining process, file, terminal, and output APIs.
- **Durable services:** run trusted, performance-sensitive processes with runc while the control plane owns replicas, health, storage, and rollouts.
- **Reproducible agent execution:** use Axrun to coordinate immutable tasks, verification, trajectories, usage, and typed artifacts.

## 📦 Install

```bash
brew install cofy-x/tap/axern
```

## 🚀 Quick Start

```bash
curl -fsSL https://raw.githubusercontent.com/cofy-x/axern/main/install.sh | sh
```

## 📚 Learn more

**Quickstart**

The supported local path runs the complete stack with Docker Compose. It needs only the `axern` CLI and Docker Compose v2 — no source checkout, Make, Helm, or language toolchains. brew install cofy-x/tap/axern Without Homebrew, use the standalone checksummed installer: curl -fsSL https://raw.githubusercontent.com/cofy-x/axern/main/install.sh | sh Then start Axern and run the first workload: axern 

**Architecture**

flowchart LR Client["CLI and SDK clients"] --> Gateway["gatewayd\npublic control and data edge"] Gateway --> Control["controld\ndurable intent and placement"] Gateway --> Tunnel["tunneld\nreverse TCP relay"] Gateway --> Node["axnoded\nsandbox execution"] Control --> Storage["storaged\nstorage control plane"] Control --> Node Storage --> Volume["volumed\nnode volume publish"] Node --> Egress["egres

**Kubernetes Install**

Axern publishes its cloud-neutral chart as an OCI artifact and the CLI as checksummed release archives. Install the chart into the current Kubernetes context: helm install axern oci://ghcr.io/cofy-x/charts/axern \ --version "$(cat VERSION)" \ --namespace axern-system \ --create-namespace \ --wait \ --timeout 15m After installing the CLI archive for your operating system, keep the gateway port-forw

## 🔗 Links

- [GitHub Repository](https://github.com/cofy-x/axern)
- [Full README](https://github.com/cofy-x/axern#readme)
- [Back to the Related Agent Harnesses list](../related.md)
