# GitHub 上传指南

这份指南适合第一次上传项目的同学。你可以选择网页上传，也可以选择命令行上传。

## 方法一：网页上传

1. 打开 GitHub，点击右上角 `+`，选择 `New repository`。
2. 仓库名填写 `ai-resume-polisher`。
3. 选择 `Public`。
4. 不要勾选 `Add a README file`，因为项目里已经有 README。
5. 创建仓库后，点击页面里的 `uploading an existing file`。
6. 把本项目文件夹里的文件拖进去。
7. 注意不要上传 `.env` 文件。
8. 点击 `Commit changes`。

## 方法二：命令行上传

进入项目目录：

```powershell
cd E:\github\ai-resume-polisher
```

初始化 Git：

```powershell
git init
git add .
git commit -m "Initial commit"
```

在 GitHub 创建同名仓库后，把仓库地址替换到下面命令里：

```powershell
git branch -M main
git remote add origin https://github.com/你的用户名/ai-resume-polisher.git
git push -u origin main
```

## 部署到 Streamlit Community Cloud

1. 打开 `https://share.streamlit.io/`。
2. 使用 GitHub 登录。
3. 点击 `New app`。
4. 选择你的仓库 `ai-resume-polisher`。
5. Main file path 填写：

```text
app.py
```

6. 如果需要 API Key，在应用设置里添加 Secrets。

Secrets 示例：

```toml
OPENAI_API_KEY = "你的 API Key"
OPENAI_BASE_URL = "https://api.openai.com/v1"
OPENAI_MODEL = "gpt-4.1-mini"
```

部署成功后，把在线体验链接放到 README 顶部。

## 简历项目描述

可以写成：

> 开发 AI 简历优化助手，基于 Streamlit 构建交互式 Web 应用，接入 OpenAI-compatible 大模型 API，实现经历输入、Prompt 构造、简历描述生成、STAR 拆解和 Markdown 下载等功能，并完成 GitHub 开源与在线部署。
