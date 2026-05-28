# AI 简历优化助手
[在线体验](https://ai-resume-polisher.streamlit.app/)
一个面向大学生的 AI 简历优化小工具。用户输入自己的原始经历、目标岗位和技能关键词，系统会调用大模型生成更专业的简历描述、STAR 拆解、岗位关键词和面试追问。

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


