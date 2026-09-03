---
title: "dsh-word-docs"
description: "Word document toolkit for DeepSeek Harness: generate, edit, extract, stat and convert .docx with a pure-stdlib Python engine (zero dependencies), registering the word_docs tool and word-docs skill. / DeepSeek Harness 的 Word 文档工具：纯 Python 标准库生成、编辑、提取、统计并转换 .docx，零依赖。"
keywords: "dsh-word-docs, developer, plugin, files, deepseek harness, dsh"
---
# dsh-word-docs

> ⭐ **0** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 0 | Status | ✅ active |
| Author | [Ei-Ayw](https://github.com/Ei-Ayw) | Updated | — |
| Subcategory | 💰 Cost & billing | Capabilities | files |

## One-liner

> Word document toolkit for DeepSeek Harness: generate, edit, extract, stat and convert .docx with a pure-stdlib Python engine (zero dependencies), registering the word_docs tool and word-docs skill. / DeepSeek Harness 的 Word 文档工具：纯 Python 标准库生成、编辑、提取、统计并转换 .docx，零依赖。

## About

**给 DeepSeek Harness 的办公 Word 文档插件——说一句话,出正式文档。** 生成、编辑、读取、统计、转 PDF `.docx`,底层是**纯 Python 标准库**(只有 `zipfile` + `xml.etree`),**零第三方依赖**——不需要 pip install 任何东西,装完即用。中文字体(宋体/eastAsia)自动处理,正式公文排版一步到位。 --- *真实生成效果(Quick Look 渲染):左=Markdown 会议纪要转公文版(页码+首行缩进+标题编号)· 中=劳动合同模板(页脚页码)· 右=周报(指定列宽表格+合并单元格+插入图片)* ---

## 📦 Install

```bash
# 1. 安装
dsh plugin --profile web add git+https://github.com/Ei-Ayw/dsh-word-docs.git

# 2. 重启 dsh Web,然后直接对 AI 说:
#    "把这份 Markdown 转成 Word,加页码、首行缩进"
#    "生成一份劳动合同模板"
#    "读一下这个 docx 里写了什么,总结一下"
#    "把这个合同里的 {占位符} 批量填掉"
```

## 🚀 Quick Start

```bash
python3 scripts/worddocs.py md2docx --input demo/sample.md --output demo/meeting.docx \
    --page-number --first-line-indent --number-headings chinese
```

## 🔗 Links

- [GitHub Repository](https://github.com/Ei-Ayw/dsh-word-docs)
- [Full README](https://github.com/Ei-Ayw/dsh-word-docs#readme)
- [Back to the Plugins list](../plugins.md)
