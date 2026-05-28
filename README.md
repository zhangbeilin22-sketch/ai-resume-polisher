# AI 简历优化助手

一个面向大学生的 AI 简历优化小工具。用户输入自己的原始经历、目标岗位和技能关键词，系统会调用大模型生成更专业的简历描述、STAR 拆解、岗位关键词和面试追问。

这个项目适合作为第一个 GitHub AI 应用项目：代码量少、成本低、容易部署，也能直接写进简历。

## 功能

- 输入目标岗位、原始经历、技能和项目亮点
- 支持生成简历 bullet point
- 支持 STAR 法则拆解
- 支持岗位关键词建议
- 支持面试追问准备
- 支持 Markdown 下载
- 没有 API Key 时也能返回演示结果，方便先跑通页面

## 技术栈

- Python
- Streamlit
- OpenAI-compatible API
- python-dotenv

## 项目结构

```text
ai-resume-polisher/
├── app.py
├── requirements.txt
├── runtime.txt
├── .env.example
├── .gitignore
├── GITHUB_UPLOAD_GUIDE.md
├── .streamlit/
│   └── config.toml
└── README.md
```

## 本地运行

1. 进入项目目录

```bash
cd ai-resume-polisher
```

2. 安装依赖

建议使用 Python 3.10 到 3.12。部署时项目会通过 `runtime.txt` 指定 Python 3.11。

```bash
pip install -r requirements.txt
```

3. 配置环境变量

复制 `.env.example` 为 `.env`，然后填入自己的 API Key。

```bash
cp .env.example .env
```

如果你使用的是 PowerShell，可以运行：

```powershell
Copy-Item .env.example .env
```

`.env` 示例：

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-4.1-mini
```

也可以在网页侧边栏里临时输入 API Key、Base URL 和模型名称。

4. 启动项目

```bash
streamlit run app.py
```

浏览器打开终端显示的本地地址，一般是：

```text
http://localhost:8501
```

## 可选模型配置

本项目使用 OpenAI 兼容接口。你可以根据自己的账号选择不同服务商。

| 服务商 | Base URL | 模型示例 |
| --- | --- | --- |
| OpenAI | `https://api.openai.com/v1` | `gpt-4.1-mini` |
| DeepSeek | `https://api.deepseek.com` | `deepseek-chat` |
| 通义千问/Qwen | `https://dashscope.aliyuncs.com/compatible-mode/v1` | `qwen-plus` |

## GitHub 上传建议

上传到 GitHub 前，建议确认：

- `.env` 不要上传
- `.env.example` 要上传
- README 保留运行步骤
- 可以在 README 里补一张项目截图
- 部署成功后，把在线体验链接放到 README 顶部

## 简历写法参考

> 开发 AI 简历优化助手，基于 Streamlit 构建交互式 Web 页面，接入 OpenAI-compatible 大模型 API，实现原始经历输入、提示词构造、简历 bullet point 生成、STAR 拆解和 Markdown 下载等功能，提升大学生简历项目表达效率。

## 后续优化方向

- 增加岗位模板，例如前端、后端、数据分析、AI 产品经理
- 增加历史记录保存功能
- 增加 PDF 简历解析功能
- 增加中英文简历切换
- 部署到 Streamlit Community Cloud 或 Hugging Face Spaces
