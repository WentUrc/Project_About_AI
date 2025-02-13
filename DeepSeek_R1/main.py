# main.py
from utils.history_manager import init_history
from core.services import get_deepseek_response_with_context


def main():
    history = init_history()
    print("【实时推理演示】")
    gen = get_deepseek_response_with_context(
        history,
        "凯留公主，刚刚我们聊了那些内容可以再详细说说吗？",
        100,
        "夕阳下的露台"
    )

    print("凯留说: ", end="", flush=True)
    if isinstance(gen, str):
        print(gen)
    else:
        for chunk in gen:
            print(chunk, end="", flush=True)


if __name__ == "__main__":
    main()
