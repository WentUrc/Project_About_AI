# config/settings.py
import os
from dotenv import load_dotenv
from openai import OpenAI
import logging

# 加载环境变量
load_dotenv()

# 初始化 OpenAI 客户端
CLIENT = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.lkeap.cloud.tencent.com/v1")

# 日志基本配置（可在 utils/logger.py 中进一步封装）
logging.basicConfig(
    filename='kailiu_chat.log',
    level=logging.INFO,
    format='【%(asctime)s】%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# 历史记录文件路径
HISTORY_FILE = 'conversation_history.json'
