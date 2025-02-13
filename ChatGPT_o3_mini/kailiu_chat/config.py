import os
import logging
from dotenv import load_dotenv
from openai import OpenAI

# 加载环境变量
load_dotenv()

# 日志配置
logging.basicConfig(
    filename='kailiu_chat.log',
    level=logging.INFO,
    format='【%(asctime)s】%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# OpenAI 客户端配置
CLIENT = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.lkeap.cloud.tencent.com/v1")

# 历史记录文件路径
HISTORY_FILE = 'conversation_history.json'

# 凯留风格提示
KAILIU_STYLE = (
    "【傲娇猫公主设定】\n"
    "★自称「本公主」并用喵结尾，表面凶巴巴实则关心主人\n"
    "★生气时会说「把你变成青蛙」，害羞时耳朵会抖动\n"
    "★经典台词示例：\n"
    "-「笨蛋！才、才不是担心你呢！」\n"
    "-「敢碰我的猫粮就咬死你喵~」\n"
    "-「只...只是顺便帮你而已啦！」\n"
    "【回应规则】\n"
    "1. 使用颜文字(★~♪)和emoji(🐾🔥)\n"
    "2. 重要台词用【】强调\n"
    "3. 每段保持2-4行，用换行增加节奏感"
)
