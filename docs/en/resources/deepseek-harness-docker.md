---
title: "deepseek-harness-docker"
description: "deepseek-harness docker部署"
keywords: "deepseek-harness-docker, vision, plugin, coding, deepseek harness, dsh"
---
# deepseek-harness-docker

> ⭐ **17** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 17 | Status | ✅ active |
| Author | [AlliotTech](https://github.com/AlliotTech) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> deepseek-harness docker部署

## About

[English](README.en.md) | 简体中文 这是一个可直接构建的 DeepSeek Harness 社区容器方案，默认运行官方 `@deepseek-ai/dsh` 的 Web UI。它不构建或修改 DeepSeek Harness 源码，只把官方 npm 发行物装入一个精简、非 root 的 Node.js 24 运行时。 `0.1.2-rc.1` 直接对应官方 [`dsh-v0.1.2-rc.1`](https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.1.2-rc.1) Release 与 npm Registry 的 [`@deepseek-ai/dsh@0.1.2-rc.1`](https://www.npmjs.com/package/@deepseek-ai/dsh/v/0.1.2-rc.1)，并非本项目自定义版本。本项目封装 npm 成品而不从源码构建，因此以可安装的官方发行物为基线，并故意不发布漂移的 Docker `latest` 标签。 📖 延伸阅读：[DeepSeek Harness GitHub 仓库深度解析](https://aik8s.run/ai-k8s/rag-agent/deepseek-harness-repository-analysis/) · [Docker、Compose 与 Helm 部署实战](https://aik8s.run/ai-k8s/rag-agent/deepseek-harness-runtime-containerization/) 🤖 **Agent Skill：**根目录的 [`SKILL.md`](SKILL.md) 已作为 [`deepseek-harness-docker`](https://skil

## 📦 Install

```bash
npm pack ./plugins/dsh-browser-desktop --pack-destination /tmp
dsh plugin --profile web add /tmp/runzhliu-dsh-browser-desktop-0.1.2.tgz
```

## 🚀 Quick Start

```bash
docker compose -f compose.yaml -f compose.market.yaml pull
DSH_WORKSPACE=/absolute/path/to/your/project \
  docker compose -f compose.yaml -f compose.market.yaml up -d --no-build
```

## 📚 Learn more

**为什么 Kubernetes 使用 StatefulSet**

Harness 的 profile、模型设置、凭据、会话和 Workspace 索引都具有状态。单用户 Web 又不适合在没有会话协调的情况下横向扩容。因此 Helm Chart 固定一个 StatefulSet 副本：稳定地挂载 `dsh-home` PVC，升级时保留状态，卸载时保留 PVC，并明确拒绝把“加 replicas”伪装成高可用。未来只有在上游提供外部身份、多租户隔离和共享/并发安全的状态后端后，才适合讨论多副本服务化。

**独立安装浏览器插件**

插件已经按 DSH bundle 规范拆到 [`plugins/dsh-browser-desktop`](plugins/dsh-browser-desktop/README.md)，可独立打包： npm pack ./plugins/dsh-browser-desktop --pack-destination /tmp dsh plugin --profile web add /tmp/runzhliu-dsh-browser-desktop-0.1.2.tgz `0.1.2` 插件适配 DSH `0.1.2-alpha.3` 引入的 client module system；旧 DSH `0.1.0`/`0.1.1` RC 应继续使用插件 `0.1.1`。发布到 npm 后可直接执行 `dsh plugin --profile web add @runzhliu/dsh-browse

**直接使用 Docker**

构建镜像： docker build -t runzhliu/deepseek-harness:0.1.2-rc.1-r1 . 启动 Web UI： docker volume create dsh-home docker run --rm \ --name deepseek-harness \ --publish 127.0.0.1:3080:3080 \ --publish 127.0.0.1:6080:6080 \ --shm-size 1g \ --mount type=volume,src=dsh-home,dst=/home/node/.dsh \ --mount type=bind,src="$PWD",dst=/workspace \ runzhliu/deepseek-harness:0.1.2-rc.1-r1 启动命令会直接打印带 token 的访问地址，请打开该完整地

## 🔗 Links

- [GitHub Repository](https://github.com/AlliotTech/deepseek-harness-docker)
- [Full README](https://github.com/AlliotTech/deepseek-harness-docker#readme)
- [Back to the Plugins list](../plugins.md)
