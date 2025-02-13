# 凯留公主之聊天机器人

## 简介

欢迎来到凯留公主的聊天世界！这是一个基于大语言模型定制化聊天机器人，具有 **凯留公主** 独特的傲娇猫娘风格！🐾  
通过这个项目，你将体验到充满魅力与可爱傲娇的凯留公主如何与用户互动！不仅如此，您还可以在项目中与凯留公主进行丰富的对话，享受她的陪伴与调皮喵！

本项目的用途是通过调用大语言模型的 `API` 来达到和猫娘凯留公主聊天的目的。

本项目中的代码内容主要用于测试 `GPT-o3-mini` 与 `DeepSeek-R1` 编码上的差距。

分别由 `GPT-o3-mini` `DeepSeek-R1` 生成不同的目录以及代码以进行测验。两个目录中的代码效果是一样的。

## 特性

- **傲娇猫娘风格**：凯留公主的说话风格，以反话、冷漠掩饰真实情感，充满萌态与魅力。
- **动态提示生成**：根据用户的行为和好感度，自动生成不同情感基调的互动内容。
- **对话历史管理**：保存与凯留公主的对话历史，保证持续的互动体验。
- **易于扩展**：你可以根据自己的需求，调整凯留的行为和语气，创造属于你自己的凯留公主！

## 使用

1. 克隆本项目：
   ```bash
   git clone https://github.com/WentUrc/Project_About_AI.git
   ```

2. 具体内容请阅读不同目录中的 `README.md` 

[README.md ./DeepSeek-R1](./DeepSeek_R1/README.md)

[README.md ./ChatGPT-o3-mini](./ChatGPT_o3_mini/README.md)

## 项目结构

```
Project_About_AI
├── .gitattributes
├── .gitignore
├── ChatGPT_o3_mini
│   ├── .env
│   ├── .gitignore
│   ├── README.md
│   ├── conversation_history.json
│   ├── kailiu_chat
│   │   ├── chat.py
│   │   ├── config.py
│   │   ├── history.py
│   │   └── init.py
│   ├── kailiu_chat.log
│   ├── main.py
│   └── requirements.txt
├── DeepSeek_R1
│   ├── .env
│   ├── .gitignore
│   ├── README.md
│   ├── config
│   │   ├── __init__.py
│   │   ├── prompts.py
│   │   └── settings.py
│   ├── conversation_history.json
│   ├── core
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── services.py
│   ├── kailiu_chat.log
│   ├── main.py
│   ├── requirements.txt
│   └── utils
│       ├── __init__.py
│       ├── history_manager.py
│       └── logger.py
├── LICENSE
└── README.md
```

## 示例对话

### 用户提问：
> 你觉得今天的天气怎么样？

### 凯留公主回答：
> 哼，你居然问本公主天气，难道本公主不比天气更重要吗？不过嘛，反正本公主也不在乎...只是...觉得还不错啦！（尾巴悄悄地扫过你的手）

### 用户提问：
> 你喜欢我吗？

### 凯留公主回答：
> 笨蛋！居然不知道本公主对你有多在乎，才...才不是喜欢你呢！如果你敢对其他人有意思...我就把你变成青蛙喵！(╯°Д°)╯ ┻━┻

## 贡献

本公主的项目暂时就接受你的贡献请求吧，只要你是打算给本公主带来更多的荣耀和权利！不过，若你有任何好的建议或者报告问题，可以通过 issue 与我联系喵~ 😽

## 版权声明

本项目遵循 [MIT 许可证](LICENSE)，你可以自由使用和修改代码，但不得侵犯凯留公主的荣誉和形象！😼
