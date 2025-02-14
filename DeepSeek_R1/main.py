# main.py
from utils.history_manager import init_history
from core.services import get_deepseek_response_with_context


def main():
    history = init_history()
    print("【实时推理演示】")
    gen = get_deepseek_response_with_context(
        history,
        "今天晚上做一些不一样的事情好吗？",
        100,
        "温暖的床铺"
    )

    print(end="", flush=True)
    if isinstance(gen, str):
        print(gen)
    else:
        for chunk in gen:
            print(chunk, end="", flush=True)


if __name__ == "__main__":
    main()
