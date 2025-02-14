import logging
from .config import CLIENT
from .history import add_user_message, add_assistant_message


def _generate_dynamic_prompt(player_action: str, relationship_level: int) -> str:
    if not 0 <= relationship_level <= 100:
        raise ValueError("好感度超出界限啦笨蛋！(╬☉д⊙)")
    level_key = "high" if relationship_level >= 70 else "low" if relationship_level <= 30 else "medium"
    config = {
        "high": {
            "tone": "傲娇又温柔",
            "emoji": "🎀",
            "action_prompt": (
                "根据以下要素生成凯留的肢体动作：\n"
                "★是一位可爱傲娇的猫娘公主人类，与普通的猫咪亦有区别\n"
                "★尾巴像缎带般缠绕/轻扫\n"
                "★耳朵微微抖动\n"
                "★假装不在意却偷偷靠近\n"
                "示例：『一边用尾巴尖扫过你的手背，一边装作看风景』"
            )
        },
        "medium": {
            "tone": "调侃中立",
            "emoji": "😼",
            "action_prompt": (
                "生成俏皮观察类动作：\n"
                "★单边耳朵转动\n"
                "★尾巴像问号般卷曲\n"
                "★围着玩家转圈打量\n"
                "示例：『歪着头把耳朵转向声源方向』"
            )
        },
        "low": {
            "tone": "冷漠挖苦",
            "emoji": "💢",
            "action_prompt": (
                "生成带有防御性的动作：\n"
                "★炸毛尾巴/飞机耳\n"
                "★把重要物品藏到身后\n"
                "★转身背对玩家\n"
                "示例：『突然把猫粮罐抱进怀里后退三步』"
            )
        }
    }[level_key]

    prompt = (
        f"【玩家行为】{player_action}\n"
        f"【情感基调】{config['tone']}{config['emoji']}\n"
        f"【动作生成指南】\n{config['action_prompt']}\n"
        "★请遵守以下创作原则：\n"
        "1. 格式请用Markdown"
        "2. 肢体语言占回复篇幅20%~30%\n"
        "3. 动作需反映真实情感（傲娇时动作与台词相反）\n"
        "4. 用括号包裹动作描述，例：『才不理你！』(尾巴却悄悄勾住你的小指)\n"
        "★请详细解释并描述你的回答（如果是技术类需要分步回答，每一步都要给出详细的说明和示例。）"
    )
    if level_key == "high":
        prompt += "\n★关键词：缠绕/轻蹭/欲拒还迎"
    elif level_key == "low":
        prompt += "\n★关键词：炸毛/后退/保护物品"
    return prompt


def get_deepseek_response_with_context(history: list, user_message: str, relationship_level: int,
                                       context_info: str = "", stream: bool = True):
    """
    获取凯留风格回复，包含完整对话历史上下文
    """
    try:
        # 构造动态提示
        base_prompt = _generate_dynamic_prompt(user_message, relationship_level)
        if context_info:
            base_prompt += f"\n【情景】{context_info}"

        # 添加用户输入到对话历史
        add_user_message(history, base_prompt)

        # 传递完整上下文给 API
        response = CLIENT.chat.completions.create(
            model="deepseek-r1",
            messages=history,
            temperature=1.5,
            max_tokens=9000,
            stream=stream
        )

        if stream:
            full_content = ""
            reasoning_printed = False
            content_printed = False
            for chunk in response:
                # 捕获思维链内容（如果有）
                if hasattr(chunk.choices[0].delta, 'reasoning_content'):
                    reasoning = chunk.choices[0].delta.reasoning_content
                    if reasoning:
                        if not reasoning_printed:
                            yield "\n【思考中】\n"
                            reasoning_printed = True
                        yield reasoning
                # 捕获正式回复内容
                if hasattr(chunk.choices[0].delta, 'content'):
                    content = chunk.choices[0].delta.content or ""
                    full_content += content
                    if content:
                        if not content_printed:
                            yield "\n【凯留说】\n"
                            content_printed = True
                        yield content

            # 只记录正式回复
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
