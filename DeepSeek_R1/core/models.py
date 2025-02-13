# core/models.py
from dataclasses import dataclass

@dataclass
class Message:
    role: str   # "system", "user", 或 "assistant"
    content: str
