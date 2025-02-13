from kailiu_chat.history import init_history
from kailiu_chat.chat import get_deepseek_response_with_context


def main():
    history = init_history()
    print("【实时推理演示】")
    gen = get_deepseek_response_with_context(
        history,
        "",
        100,
        "温暖的床铺"
    )

    print("凯留公主说: ", end="", flush=True)
    # 流式输出
    if isinstance(gen, str):
        print(gen)
    else:
        for chunk in gen:
            print(chunk, end="", flush=True)


if __name__ == "__main__":
    main()
