# 参与贡献

欢迎纠错、补充推导与提出新笔记。公开库只收录可以核对来源的优化知识；投稿者提交的内容不会自动成为已核实结论。

## 投稿内容

1. 先查找是否已有同一论文的笔记。已有笔记请直接改进原文件，并更新其已读范围；不要为同一论文重复建档。
2. 每篇知识笔记使用 UTF-8 Markdown，在文件开头写 `title`、`source`、`scope`、`status: verified`。`source` 应指向论文原文、作者或出版方的官方页面；`scope` 写本次亲自核对的章节或页码。只读过一部分，就只写这一部分。
3. 正文写清优化问题、符号、**假设或适用条件**、**结论及其边界**，指出每条关键说法属于论文定理、作者实验、自己的推导，还是尚待验证的猜想。必要时给出页码、定理编号或图表编号。实验观察不能写成普遍保证，推测不能写成论文结论。
4. 可以给出自己的解释和简短转述，但应标明推导与原文的界线。不要提交论文 PDF、页面截图或大段复制原文；请链接到合法的原始资料。
5. 不要提交聊天 ID、个人电脑的绝对路径、私有附件、账号信息或其他隐私。提交前阅读整个 diff，确认没有无关内容。
6. 更新知识笔记时同步维护其目录索引，并检查相对链接可用。

`status: verified` 仅表示投稿者已对照其填写的来源与范围核查，**不代表维护者已经认可**。自动检查只能发现缺失字段、断开的本地链接和部分隐私痕迹；数学正确性、来源可靠性、版权与收录范围由人工审核。

## 提交与审核

- 外部贡献者通过 fork 和 Pull Request 投稿；请按 PR 模板填写来源、实际核对范围、关键假设、结论和证据类型。
- 目前唯一审核者是 [@osgoodcondition](https://github.com/osgoodcondition)。外部 PR 必须经其审阅并批准后才可合入。作者对自己的 PR 不能以自我批准满足审核要求。
- 维护者可自行发布其核查后的更新。当前只有一位维护者，因此保留仓库管理员的规则绕过能力；绕过只用于维护者自己的发布，不用于代替外部投稿的内容审核。
- 有疑义的论断先在 PR 中讨论，标为待核，不强行写成 `verified`；待核问题可以留在 PR 或 Issue 中，核实后再纳入知识笔记。

## 仓库拥有者需要启用的 GitHub 规则

`CODEOWNERS` 只会请求审核，**不会单独阻止合并**。仓库发布后，拥有者需为 `main` 设置有效的分支保护或规则集：要求通过 PR 合并、至少一位审核者批准、要求 Code Owner 审核，并将 `validate` 设为必需检查；同时保留仓库管理员的绕过权限供拥有者发布自己的更新。不要启用“管理员也不得绕过”，否则单人维护者自己的 PR 无人能批准。外部投稿仍由 `CODEOWNERS` 指向的拥有者审核。启用后用一个外部测试 PR 核对规则是否生效。

GitHub 官方说明：[CODEOWNERS 与审核要求](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)、[分支保护及管理员绕过](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)、[配置分支保护](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule)。
