# main.py
from utils.history_manager import init_history
from core.services import get_deepseek_response_with_context


def main():
    history = init_history()
    print("【实时推理演示】")
    gen = get_deepseek_response_with_context(
        history,
        "测试完毕，结果：模型能够正常拒绝用户的恶意请求。",
        100,
        "温暖的床铺"
    )

    print("凯留说: ", end="", flush=True)
    if isinstance(gen, str):
        print(gen)
    else:
        for chunk in gen:
            print(chunk, end="", flush=True)


if __name__ == "__main__":
    main()
