# 课本习题截图转 Word Skill

把教材 PDF 中指定题号的题干、公式和配图裁成图片，生成与示例相同的 A4 作业文档：标题为 `Homework N`，一题一页，下面留出手写作答空间。不解题。跨页题目可按阅读顺序拼接。

## 分享链接

- [Skill 文件夹](https://github.com/Victor-GitHup/textbook-problems-to-word-skill/tree/main/textbook-problems-to-word)
- [下载 ZIP](https://github.com/Victor-GitHup/textbook-problems-to-word-skill/archive/refs/heads/main.zip)

这个仓库只含 Skill 和脚本，不含教材或作业题目图片。

## 发给 AI 的第一条消息

复制下面整段，将链接发给具有联网、读取文件、运行代码和生成 `.docx` 能力的 AI：

> 请从 https://github.com/Victor-GitHup/textbook-problems-to-word-skill/tree/main/textbook-problems-to-word 下载并启用 `textbook-problems-to-word` Skill。读取 `SKILL.md` 和它引用的文件；按当前平台的方式安装 Skill，或在本次会话加载整个目录。安装 `requirements.txt` 中缺少的 Python 包及 Poppler 的 `pdftoppm`，运行 `scripts/check_environment.py`。确认你能读取我随后上传的文件、运行生成脚本并交付 Word 文档。全部成功后，只回复：“已安装完成，请上传习题来源文件以及作业对应题号”。如果缺少这些能力或检查失败，请具体说明，不能宣称安装成功。之后我上传教材 PDF 与题号时，请按 Skill 生成并逐页检查 Word 文件，不需要解题。

Codex 用户也可直接让 `$skill-installer` 从上面的 Skill 文件夹链接安装。Claude Code 用户可把 `textbook-problems-to-word` 整个文件夹放到 `~/.claude/skills/`。仅有普通文本聊天功能、不能读取附件或执行脚本的 AI 无法完成此流程。

如果 AI 不能直接访问 GitHub，先由同学下载 ZIP，再把 ZIP 作为附件上传给 AI，并发送同一段提示词。

## 收到安装完成回复后

上传教材 PDF，并列出作业标题、印刷页码和题号。例如：

> Homework 3：P117 Problem 3.20；P122 Problem 3.55；P167 Problem 4.44。请只交付包含题目截图与作答空白的 Word 文档。

如果题号所在页没有完整配图，应让 AI 在邻页找齐；若版本或页码不匹配，应先说明并核对，不应猜题。若某题有教师补充要求，把原文一并发给 AI。

## 本地依赖

- Python 3、`requirements.txt` 列出的包、Poppler 的 `pdftoppm`。
- 有 Word/PDF 渲染能力的环境，供逐页检查；例如 LibreOffice。

安装 Python 包后，在 Skill 文件夹运行 `python3 scripts/check_environment.py`。核心生成脚本为 `scripts/make_homework.py`，输入为人工核对过裁切范围的 JSON 配方。完整流程和示例见 `SKILL.md`。
