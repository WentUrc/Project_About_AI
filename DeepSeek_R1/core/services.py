# core/services.py
import logging
from config.settings import CLIENT
from config.prompts import generate_dynamic_prompt
from utils.history_manager import add_user_message, add_assistant_message


def get_deepseek_response_with_context(history: list, user_message: str, relationship_level: int,
                                       context_info: str = "", stream: bool = True):
    """
    获取凯留风格回复，基于完整对话历史上下文。
    """
    try:
        base_prompt = generate_dynamic_prompt(user_message, relationship_level)
        if context_info:
            base_prompt += f"\n【情景】{context_info}"

        add_user_message(history, base_prompt)

        response = CLIENT.chat.completions.create(
            model="deepseek-r1",
            messages=history,
            temperature=1.5,
            max_tokens=9000,
            stream=stream
        )

        if stream:
            full_content = ""
            reasoning_log = []
            for chunk in response:
                # 捕获思维链（可选输出）
                if hasattr(chunk.choices[0].delta, 'reasoning_content'):
                    reasoning = chunk.choices[0].delta.reasoning_content
                    if reasoning:
                        reasoning_log.append(f"🧠 思考轨迹: {reasoning}")
                        yield reasoning
                # 捕获正式回复
                if hasattr(chunk.choices[0].delta, 'content'):
                    content = chunk.choices[0].delta.content or ""
                    full_content += content
                    if content:
                        yield content

            add_assistant_message(history, full_content)
            logging.info(f"Player: {user_message} → Kailiu: {full_content[:200]}...")
            return full_content
        else:
            reply = response.choices[0].message.content.strip()
            add_assistant_message(history, reply)
            logging.info(f"Player: {user_message} → Kailiu: {reply[:50]}...")
            return reply

    except Exception as e:
        error_msg = f"{type(e).__name__}: {str(e)}"
        logging.error(f"API调用失败 ❌ {error_msg}")

        if hasattr(e, 'APIError'):
            return "呜...服务器炸毛了啦！(跺脚)待会再试喵！(＞﹏＜)"
        elif isinstance(e, TimeoutError):
            return "等...等太久了！本公主不等了喵！(╯°Д°)╯ ┻━┻"
        else:
            return "有个bug在挠我的尾巴！快检查日志喵~ (=；ェ；=)"
