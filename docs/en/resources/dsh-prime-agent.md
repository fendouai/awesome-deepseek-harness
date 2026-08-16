---
title: "dsh-prime-agent"
description: "Prime Agent-inspired persistent RLM control plane for DSH Code Mode."
keywords: "dsh-prime-agent, workflow, deepseek harness, dsh"
---
# dsh-prime-agent

> ⭐ 3 · ✅ active · workflow

## One-liner

Prime Agent-inspired persistent RLM control plane for DSH Code Mode.

## About

<p align="center"> </p> - 插件注册固定名称的 `prime_realm_identity` bootstrap binding。`PrimeCodeRuntime` 在执行程序前以 32 字节 CSPRNG challenge 调用它,验证带 session binding 的 HMAC proof 后,才把请求路由到该会话的持久 Realm Worker。 - 没有该 binding 的请求原样委托官方 one-shot Worker;binding 存在但握手失败时明确报错,绝不静默降级。 - Realm 内的工具经跨 run 稳定的 Proxy 与 per-run binding lease 调用:schema、审批、沙箱、日志、并发和取消仍由 DSH 执行,run 结束立即撤销授权。 - Realm 是 live-only 的:abort、timeout、OOM 会 hard-kill Worker 并丢失 heap,下一次 run 收到明确的 generation 通知。跨重启的检查点由程序显式写入持久任务文件。 完整身份协议、generation 

## Author
**[yoke233](https://github.com/yoke233)**

## Links

- [GitHub Repository](https://github.com/yoke233/dsh-prime-agent)
- [Full README](https://github.com/yoke233/dsh-prime-agent#readme)
- [Back to the Workflows & Automation list](../workflows.md)
