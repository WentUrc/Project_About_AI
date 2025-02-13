# utils/history_manager.py
import os
import json
import logging
from config.settings import HISTORY_FILE
from config.prompts import KAILIU_STYLE

def load_history() -> list:
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
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def init_history() -> list:
    history = load_history()
    if not history:
        history = [{"role": "system", "content": KAILIU_STYLE}]
        save_history(history)
    return history

def add_user_message(history: list, message: str):
    history.append({"role": "user", "content": message})
    save_history(history)

def add_assistant_message(history: list, message: str):
    history.append({"role": "assistant", "content": message})
    save_history(history)
