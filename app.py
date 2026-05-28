import os
from textwrap import dedent

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


PROVIDER_PRESETS = {
    "OpenAI": {
        "base_url": "https://api.openai.com/v1",
        "model": "gpt-4.1-mini",
    },
    "DeepSeek": {
        "base_url": "https://api.deepseek.com",
        "model": "deepseek-chat",
    },
    "通义千问/Qwen": {
        "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "model": "qwen-plus",
    },
    "自定义 OpenAI 兼容接口": {
        "base_url": os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
        "model": os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
    },
}


st.set_page_config(
    page_title="AI 简历优化助手",
    page_icon="📝",
    layout="wide",
)


def build_prompt(role, experience, skills, highlights, style, language):
    return dedent(
        f"""
        你是一位有经验的校园招聘简历导师。请根据用户提供的信息，帮助优化简历中的项目/经历描述。

        目标岗位：{role}
        原始经历：{experience}
        已掌握技能：{skills}
        亮点或成果：{highlights}
        表达风格：{style}
        输出语言：{language}

        请按以下结构输出：
        1. 简历优化版描述：给出 3-5 条可以直接放进简历的项目经历 bullet point。
        2. STAR 拆解：分别说明情境、任务、行动、结果。
        3. 关键词建议：列出适合该岗位的技能关键词。
        4. 可补充的数据指标：告诉用户还能补充哪些量化信息。
        5. 面试追问准备：生成 3 个面试官可能会问的问题。

        要求：
        - 不要编造不存在的公司、奖项、用户数量或夸张结果。
        - 如果用户没有提供量化数据，请用“可补充：...”提示。
        - 表达要专业、简洁、适合大学生简历。
        """
    ).strip()


def call_llm(provider, api_key, base_url, model, prompt):
    client = OpenAI(api_key=api_key, base_url=base_url)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "你是一位务实、专业的大学生求职简历导师。",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.4,
    )
    return response.choices[0].message.content


def demo_output(role, experience, skills):
    return f"""
## 1. 简历优化版描述

- 面向 **{role or "目标岗位"}** 场景，独立完成项目需求分析、功能设计与基础实现，提升了对真实业务问题的拆解能力。
- 使用 **{skills or "Python / Streamlit / 大模型 API"}** 构建交互式 AI 工具，实现用户输入、提示词组织、模型调用与结果展示等核心流程。
- 针对原始经历“{experience[:50] if experience else "待补充"}...”进行结构化整理，将项目背景、个人职责和产出结果转化为更适合简历展示的表达。
- 通过 README、运行说明和示例截图完善 GitHub 项目展示，增强项目的可复现性和求职展示价值。

## 2. STAR 拆解

- 情境：缺少可展示的 AI 应用项目，需要通过低成本项目提升简历竞争力。
- 任务：设计并实现一个面向求职场景的 AI 简历优化工具。
- 行动：使用 Streamlit 搭建网页界面，调用大模型 API 生成简历优化建议。
- 结果：形成可运行、可部署、可写进简历的完整 GitHub 项目。

## 3. 关键词建议

`AI 应用开发`、`Prompt Engineering`、`Streamlit`、`OpenAI-compatible API`、`简历优化`、`人机交互`

## 4. 可补充的数据指标

- 可补充：项目开发周期，例如“3 天完成 MVP”。
- 可补充：支持的岗位数量，例如“支持 6 类常见岗位模板”。
- 可补充：测试样例数量，例如“整理 20 条简历样例进行测试”。

## 5. 面试追问准备

1. 你是如何设计提示词，让输出更适合简历场景的？
2. 如果模型生成了夸大的内容，你如何控制风险？
3. 这个项目后续还可以怎么改进？
"""


st.title("AI 简历优化助手")
st.caption("输入你的经历，生成更适合放进简历和 GitHub 项目介绍的表达。")

with st.sidebar:
    st.header("模型设置")
    provider = st.selectbox("服务商", list(PROVIDER_PRESETS.keys()))
    preset = PROVIDER_PRESETS[provider]

    default_api_key = os.getenv("OPENAI_API_KEY", "")
    api_key = st.text_input("API Key", value=default_api_key, type="password")
    base_url = st.text_input("Base URL", value=preset["base_url"])
    model = st.text_input("模型名称", value=preset["model"])

    st.divider()
    st.write("没有 API Key 也可以点击生成，应用会返回一份演示结果。")


left, right = st.columns([1, 1])

with left:
    role = st.text_input("目标岗位", placeholder="例如：AI 应用开发实习生 / 后端开发实习生")
    style = st.selectbox("表达风格", ["简洁专业", "技术突出", "校园招聘友好", "偏产品运营"])
    language = st.selectbox("输出语言", ["中文", "英文"])
    skills = st.text_area(
        "你会的技能",
        placeholder="例如：Python、Streamlit、基础前端、Git、SQL",
        height=110,
    )

with right:
    experience = st.text_area(
        "原始经历",
        placeholder="把你做过的课程设计、比赛、小工具、社团经历写在这里。哪怕很普通也可以。",
        height=170,
    )
    highlights = st.text_area(
        "亮点或成果",
        placeholder="例如：完成了网页部署、整理了 20 条测试样例、提升了使用效率等。没有也可以空着。",
        height=110,
    )


generate = st.button("生成优化方案", type="primary", use_container_width=True)

if generate:
    if not role.strip() and not experience.strip():
        st.warning("建议至少填写目标岗位和一段原始经历，这样生成效果会更好。")
    else:
        prompt = build_prompt(role, experience, skills, highlights, style, language)
        with st.spinner("AI 正在整理你的经历..."):
            if api_key.strip():
                try:
                    result = call_llm(provider, api_key, base_url, model, prompt)
                except Exception as exc:
                    st.error("模型调用失败。请检查 API Key、Base URL 和模型名称。")
                    st.exception(exc)
                    result = ""
            else:
                result = demo_output(role, experience, skills)

        if result:
            st.subheader("优化结果")
            st.markdown(result)
            st.download_button(
                "下载 Markdown",
                data=result,
                file_name="resume-polished.md",
                mime="text/markdown",
                use_container_width=True,
            )


with st.expander("示例输入"):
    st.markdown(
        """
        **目标岗位**：AI 应用开发实习生

        **技能**：Python、Streamlit、Git、Prompt Engineering、基础 HTML/CSS

        **原始经历**：我做了一个简历优化小工具，用户输入自己的经历后，可以调用大模型生成更专业的简历描述。

        **亮点或成果**：完成网页界面、支持 API Key 配置、可以下载 Markdown 结果。
        """
    )
