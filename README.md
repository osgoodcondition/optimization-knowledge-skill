# Optimization Knowledge

一个面向优化研究与学习的轻量 Codex skill 插件。它提供**经过来源核对的笔记**和论文阅读流程；使用时先查索引，再按需读取相关笔记，不会一次加载整库。无需 Obsidian、MCP 服务或额外运行环境。

> 首版只包含少量已核实的基础笔记。GitHub 插件来源与 OpenAI 官方公共插件目录是不同的发布渠道。

## 内容边界

- `plugins/optimization-knowledge/skills/optimization-knowledge/references/` 只收录已审阅的通用知识。每篇标明原始来源、实际核对的章节或页码，以及证据边界。
- 未核实的论文定理、个人聊天记录、个人学习规划、电脑路径、论文 PDF 与截图不进入公开插件。
- 用户自己的阅读笔记保存在**自己指定的文件夹**。安装后的公共笔记是发行版，不把未经审核的新内容直接写进去。
- 插件协助阅读和整理，不代替核对原论文，也不会在后台自动通读用户的文件。

## 安装

在支持 GitHub 插件市场的 Codex 中执行：

```text
codex plugin marketplace add osgoodcondition/optimization-knowledge-skill
codex plugin add optimization-knowledge@osgoodcondition-plugins
```

也可在 Codex 插件目录中选择 `osgoodcondition Plugins` 来源，再安装 `Optimization Knowledge`。安装后可正常提问优化问题，或显式使用 `$optimization-knowledge`。

此仓库只提供 GitHub 插件来源；若未来申请进入 OpenAI 官方公共插件目录，会另行说明审核及发布状态。

## 获取新版

关注仓库的 **Watch → Custom → Releases** 可收到版本通知。看到新版后执行：

```text
codex plugin marketplace upgrade osgoodcondition-plugins
```

这会刷新 GitHub 插件来源；如当前聊天仍显示旧内容，请开始新聊天或重启 Codex。版本以 GitHub Release 和 `plugin.json` 的版本号为准。更新由用户主动触发，避免在研究过程中悄悄改变参考内容。

## 投稿和审核

欢迎通过 fork 与 Pull Request 纠错或补充。请先读 [贡献说明](CONTRIBUTING.md)，给出可公开的一手来源、精确阅读范围、假设与结论，并区分定理、实验和自己的解释。自动检查只核对格式、链接和明显的私人信息；数学内容由维护者人工审核。外部投稿在审核通过前不会进入发行版。

维护者分工见 [MAINTAINERS.md](MAINTAINERS.md)。首版由 [@osgoodcondition](https://github.com/osgoodcondition) 审核，之后可增加共同维护者。

## 许可证

原创知识笔记、skill 指令与文档采用 [CC BY-SA 4.0](LICENSE)：转载或改编时需署名，并以相同方式共享。仓库中的验证脚本采用 [MIT](LICENSE-CODE)。原论文、图表与第三方资料仍归各自权利人所有，不因本仓库的许可而改变。
