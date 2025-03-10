# 凯留公主之聊天机器人

## 简介

该目录由 `DeepSeek-R1` 生成，用来和同仓库中 `ChatGPT-o3-mini` 模型生成的 `ChatGPT-o3-mini` 目录进行编码对比，以测验两者编码上的差距。实际上本目录结构由 `DeepSeek_R1` 生成，但是 `R1` 将代码仅生成了部分，不像 `o3-mini` 不仅将目录结构生成出来，还一次性的将目录中的所有文件的代码完整地生成出来。所以本目录的代码部分是由 `o3-mini` 完成的。

## 特性

- **傲娇猫娘风格**：凯留公主的说话风格，以反话、冷漠掩饰真实情感，充满萌态与魅力。
- **动态提示生成**：根据用户的行为和好感度，自动生成不同情感基调的互动内容。
- **对话历史管理**：保存与凯留公主的对话历史，保证持续的互动体验。
- **易于扩展**：你可以根据自己的需求，调整凯留的行为和语气，创造属于你自己的凯留公主！

## 安装

1. 克隆本项目：
   ```bash
   git clone https://github.com/WentUrc/Project_About_AI.git
   ```

2. `cd` 进入 `DeepSeek_R1` 文件夹:
   ```bash
   cd ./DeepSeek_R1
   ```

3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

4. 配置环境变量：
   
   在 `DeepSeek_R1` 目录下创建 `.env` 文件，并在其中设置你的 API Key：
   ```ini
   DEEPSEEK_API_KEY=<your_api_key_here>
   ```

5. 配置你的大语言模型服务接口：
   在 `/config` 中找到 `settings.py` 并打开修改 `base_url`，例如：
   ```Python
   # 初始化 OpenAI 客户端
   CLIENT = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.lkeap.cloud.tencent.com/v1")
   ```

## 使用

### 启动示例

1. 编辑当前目录中的 `main.py` 里的：
   ```Python
   def main():
    history = init_history()
    print("【实时推理演示】")
    gen = get_deepseek_response_with_context(
        history,
        "凯留公主，刚刚我们聊了那些内容可以再详细说说吗？", # 这里写入你想对凯留公主说的话，等同于对话框
        100,                                            # 这里是凯留公主对你的好感度，可以修改
        "夕阳下的露台"                                   # 这里是聊天场景，可以修改
    )

    print("凯留说: ", end="", flush=True)
    if isinstance(gen, str):
        print(gen)
    else:
        for chunk in gen:
            print(chunk, end="", flush=True)
   ```

2. 在终端运行主程序：
   ```bash
   python3 main.py
   ```

3. 然后，你将看到凯留公主开始和你互动啦！🎀

## 项目结构

```
DeepSeek_R1/
├── config/
│   ├── __init__.py
│   ├── settings.py       # 配置管理
│   └── prompts.py        # 提示模板配置
├── core/
│   ├── __init__.py
│   ├── models.py         # 数据模型定义
│   └── services.py       # 核心业务逻辑
├── utils/
│   ├── __init__.py
│   ├── logger.py         # 日志配置
│   └── history_manager.py # 历史记录管理
├── main.py               # 主程序入口
└── requirements.txt      # 依赖列表
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

## 开发者指南

如果你想为凯留公主添加新功能或调整她的行为，可以参考以下步骤：

1. **调整提示模板**：在 `config/prompts.py` 中修改凯留的风格和台词。
2. **扩展模型交互**：在 `core/services.py` 中修改与 OpenAI 的交互逻辑，增强凯留的智能。
3. **历史记录**：通过 `utils/history_manager.py` 管理和存储与凯留的对话历史。
4. **日志系统**：在 `utils/logger.py` 中进行日志配置，跟踪开发过程中发生的所有事件。

## 贡献

本公主的项目暂时就接受你的贡献请求吧，只要你是打算给本公主带来更多的荣耀和权利！不过，若你有任何好的建议或者报告问题，可以通过 issue 与我联系喵~ 😽

## 致谢

感谢强大的大语言模型支持，使得凯留公主的智慧得以展现！  
感谢所有为这个项目贡献想法和代码的开发者，你们的努力让本公主变得更加完美！🎀

## 版权声明

本项目遵循 [MIT 许可证](LICENSE)，你可以自由使用和修改代码，但不得侵犯凯留公主的荣誉和形象！😼
