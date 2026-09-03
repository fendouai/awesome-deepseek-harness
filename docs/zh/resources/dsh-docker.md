---
title: "dsh-docker"
description: "DeepSeek Harness 容器管理插件：docker_ps/logs/inspect/exec/manage 五工具，官方 subprocess 服务、argv 无 shell 注入、exec 审批门、零运行时依赖。· Containers for DeepSeek Harness agents."
keywords: "dsh-docker, vision, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-docker

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [STARDUSTLC666](https://github.com/STARDUSTLC666) | 更新时间 | 2026-08-18 |
| 子分类 | 👁️ 视觉工具 | 能力 | coding, multi-agent |

## 一句话介绍

> DeepSeek Harness 容器管理插件：docker_ps/logs/inspect/exec/manage 五工具，官方 subprocess 服务、argv 无 shell 注入、exec 审批门、零运行时依赖。· Containers for DeepSeek Harness agents.

## 详细介绍

DSH（DeepSeek Harness）容器管理插件：走官方 subprocess 服务跑 docker CLI，argv 数组无 shell 注入，`docker_exec` 默认审批门，**零运行时依赖**。

## 📦 安装

```bash
dsh plugin --profile web add @stardustlc/dsh-docker
```

## 🚀 快速开始

```bash
dsh plugin --profile web remove @stardustlc/dsh-docker
```

## 📚 更多信息

**安装**

dsh plugin --profile web add @stardustlc/dsh-docker 需要本机装有 Docker（`docker version` 能出结果即可）；不在 PATH 上时用 `dockerPath` 指定。

**配置**

name: '@stardustlc/dsh-docker' config: # dockerPath: C:\Program Files\Docker\Docker\resources\bin\docker.exe dockerPath: docker # 可选；也可用环境变量 DSH_DOCKER_PATH timeoutMs: 60000 # 单次操作超时（默认 60 秒，5 秒 - 10 分钟） # execApproval: false # 关闭 docker_exec 审批门（默认 true）

**示例**

docker_ps {} docker_ps { all: true, name: web } docker_images { dangling: true } docker_logs { container: web, tail: 200 } docker_inspect { container: web } docker_exec { container: web, command: 'df -h' } docker_manage { container: web, action: restart }

## 🔗 链接

- [GitHub 仓库](https://github.com/STARDUSTLC666/dsh-docker)
- [完整 README](https://github.com/STARDUSTLC666/dsh-docker#readme)
- [返回dsh-docker所在分类](../plugins.md)
