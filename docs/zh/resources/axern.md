---
title: "Axern"
description: "面向 AI Agent 的开源沙箱：不可信代码执行与持久服务。"
keywords: "Axern, harness, related, security, deepseek harness, dsh"
---
# Axern

> ⭐ **57** · ✅ 活跃 · 相关 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 相关 | 分类 | Harness |
| 星数 | ⭐ 57 | 状态 | ✅ 活跃 |
| 作者 | [cofy-x](https://github.com/cofy-x) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 面向 AI Agent 的开源沙箱：不可信代码执行与持久服务。

## 详细介绍

The supported local path runs the complete stack with Docker Compose. It needs only the `axern` CLI and Docker Compose v2 — no source checkout, Make, Helm, or language toolchains. brew install cofy-x/tap/axern Without Homebrew, use the standalone checksummed installer: curl -fsSL https://raw.githubusercontent.com/cofy-x/axern/main/install.sh | sh Then start Axern and run the first workload: axern local up axern local image load python:3.12-slim --pull axern run python:3.12-slim -- python -c 'print("hello from axern")' `local up` starts PostgreSQL, MinIO, the control and node services, waits for readiness, and creates the `local` context. `local image load` streams the selected host Docker image into that local node without a temporary archive: axern context current axern run list axern loc

## ✨ 核心特性

- **Agent sandboxes:** execute agent-generated code behind a runsc isolation boundary while retaining process, file, terminal, and output APIs.
- **Durable services:** run trusted, performance-sensitive processes with runc while the control plane owns replicas, health, storage, and rollouts.
- **Reproducible agent execution:** use Axrun to coordinate immutable tasks, verification, trajectories, usage, and typed artifacts.

## 📦 安装

```bash
brew install cofy-x/tap/axern
```

## 🚀 快速开始

```bash
curl -fsSL https://raw.githubusercontent.com/cofy-x/axern/main/install.sh | sh
```

## 📚 更多信息

**Quickstart**

The supported local path runs the complete stack with Docker Compose. It needs only the `axern` CLI and Docker Compose v2 — no source checkout, Make, Helm, or language toolchains. brew install cofy-x/tap/axern Without Homebrew, use the standalone checksummed installer: curl -fsSL https://raw.githubusercontent.com/cofy-x/axern/main/install.sh | sh Then start Axern and run the first workload: axern 

**Architecture**

flowchart LR Client["CLI and SDK clients"] --> Gateway["gatewayd\npublic control and data edge"] Gateway --> Control["controld\ndurable intent and placement"] Gateway --> Tunnel["tunneld\nreverse TCP relay"] Gateway --> Node["axnoded\nsandbox execution"] Control --> Storage["storaged\nstorage control plane"] Control --> Node Storage --> Volume["volumed\nnode volume publish"] Node --> Egress["egres

**Kubernetes Install**

Axern publishes its cloud-neutral chart as an OCI artifact and the CLI as checksummed release archives. Install the chart into the current Kubernetes context: helm install axern oci://ghcr.io/cofy-x/charts/axern \ --version "$(cat VERSION)" \ --namespace axern-system \ --create-namespace \ --wait \ --timeout 15m After installing the CLI archive for your operating system, keep the gateway port-forw

## 🔗 链接

- [GitHub 仓库](https://github.com/cofy-x/axern)
- [完整 README](https://github.com/cofy-x/axern#readme)
- [返回Axern所在分类](../related.md)
