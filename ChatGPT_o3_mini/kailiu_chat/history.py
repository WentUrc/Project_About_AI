import os
import json
import logging
from .config import HISTORY_FILE, KAILIU_STYLE

def load_history() -> list:
    """从文件中加载历史记录，如果文件不存在则返回空列表"""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            try:
                history = json.load(f)
                if isinstance(history, list):
                    return history
            except json.JSONDecodeError:
                logging.error("历史记录文件格式错误，加载失败。")
    return []

def save_history(history: list):
    """将历史记录保存到文件中"""
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def init_history() -> list:
    """初始化历史记录：若文件中无记录则写入系统提示"""
    history = load_history()
    if not history:
        history = [{"role": "system", "content": KAILIU_STYLE}]
        save_history(history)
    return history

def add_user_message(history: list, message: str):
    """添加用户消息并保存"""
    history.append({"role": "user", "content": message})
    save_history(history)

def add_assistant_message(history: list, message: str):
    """添加助手消息并保存"""
    history.append({"role": "assistant", "content": message})
    save_history(history)
