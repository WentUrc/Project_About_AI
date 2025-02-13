# 凯留公主之聊天机器人

## 目录介绍

该目录由 `GPT-o3-mini` 生成，用来和同仓库中 `DeepSeek-R1` 模型生成的 `DeepSeek_R1` 目录进行编码对比，以测验两者编码上的差距。

## 特性

- **凯留风格对话**：凯留公主的说话风格充满了傲娇、冷漠和萌态，适应不同好感度的情感基调。
- **对话历史管理**：自动保存与凯留的对话历史，确保持续对话体验。
- **轻松使用**：通过简单配置和运行，你可以快速启动聊天机器人。

## 安装

1. 克隆项目仓库：
   ```bash
   git clone https://github.com/WentUrc/Project_About_AI.git
   ```

2. `cd` 进入 `ChatGPT_o3_mini` 文件夹:
   ```bash
   cd ./ChatGPT_o3_mini
   ```

3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

4. 配置环境变量：
   
   在 `ChatGPT_o3_mini` 目录下创建 `.env` 文件，并在其中设置你的 API Key：
   ```ini
   DEEPSEEK_API_KEY=<your_api_key_here>
   ```
5. 配置你的大语言模型服务接口：
   
   在 `/kailiu_chat` 中找到 `config.py` 并打开修改 `base_url`，例如：
   ```Python
   # OpenAI 客户端配置
   CLIENT = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.lkeap.cloud.tencent.com/v1")
   ```

## 使用

### 启动聊天

1. 编辑当前目录中的 `main.py`里的：
   ```Python
   def main():
    history = init_history()
    print("【实时推理演示】")
    gen = get_deepseek_response_with_context(
        history,
        "凯留公主，刚刚我们聊了那些内容可以再详细说说吗？",   # 这里写入你想对凯留公主说的话，等同于对话框
        100,                                              # 这里是凯留公主对你的好感度，可以修改
        "温暖的床铺"                                       # 这里是聊天场景，可以修改
    )

    print("凯留公主说: ", end="", flush=True)
    # 流式输出
    if isinstance(gen, str):
        print(gen)
    else:
        for chunk in gen:
            print(chunk, end="", flush=True)
   ```

2. 运行该目录中的 `main.py` 启动聊天：
   ```bash
   python3 main.py
   ```

3. 程序启动后，凯留公主将根据你的输入进行对话。🎀

## 项目结构

```
ChatGPT_o3_mini/
├── .env                  # 存储 API 密钥等环境变量
├── README.md             # 项目文档
├── requirements.txt      # Python 项目依赖
├── main.py               # 主程序入口
└── kailiu_chat
    ├── __init__.py       # 包初始化
    ├── config.py         # 配置文件，加载环境变量和配置
    ├── history.py        # 历史记录管理（加载、保存对话历史）
    └── chat.py           # 核心聊天逻辑与接口交互
```

## 示例对话

### 用户提问：
> 你喜欢我吗？

### 凯留公主回答：
> 哼，你这个笨蛋，居然问我这个问题！我才...才不是喜欢你呢！不过...如果你敢去勾搭别人，我就把你变成青蛙喵！(╯°Д°)╯ ┻━┻

## 开发

### 主要模块

- **config.py**：管理环境变量和配置项。包含与 OpenAI 的连接设置以及 API 密钥。
- **history.py**：用于管理聊天记录，包括加载历史记录和保存对话历史，以便维持持续的对话体验。
- **chat.py**：核心聊天逻辑，负责处理用户输入并与 OpenAI 接口交互，生成凯留公主的风格化回复。

## 贡献

目前本项目接受外部贡献，但如果你有任何改进建议或遇到问题，欢迎通过 GitHub 提交 Issue 或 Pull Request 与我们联系！😽

## 版权声明

本项目遵循 [MIT 许可证](LICENSE)，你可以自由使用和修改代码，但请务必尊重凯留公主的形象与魅力！😼