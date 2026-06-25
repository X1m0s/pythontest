import random
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def leet_name(name: str, probability: float = 0.6) -> str:
    table = str.maketrans(
        "iIoOzZeEaAsSbBqT",
        "1100223344556697"
    )
    full_leet = name.translate(table)
    result = []
    for orig, leet_ch in zip(name, full_leet):
        if orig != leet_ch and random.random() < probability:
            result.append(leet_ch)
        else:
            result.append(orig)
    return ''.join(result)


if __name__ == "__main__":
    prob = 0.6
    last_original = ""
    last_new = ""

    while True:
        clear()
        pct = f"{int(prob * 100)}%"
        lines = [
            "英文名称 Leet 随机转换器",
            f"当前替换概率: {pct}",
            "输入 ':p 0.8' 调整概率",
            "输入 ':q' 退出",
        ]
        width = 44  # 固定宽度，中英文混合稳妥对齐
        border = "╔" + "═" * (width - 2) + "╗"
        bottom = "╚" + "═" * (width - 2) + "╝"
        print(border)
        for line in lines:
            dsp = sum(2 if ord(c) > 127 else 1 for c in line)
            pad = width - 4 - dsp   # 4 = ║ + 空格 + 空格 + ║ 各占1列
            print(f"║ {line}{' ' * pad} ║")
        print(bottom)
        if last_original:
            print(f"  上一次转换: {last_original} --> {last_new}\n")

        raw = input("  名称 > ").strip()
        if not raw:
            continue
        if raw == ":q":
            print("\n  再见")
            break
        if raw.startswith(":p"):
            try:
                prob = float(raw.split()[1])
                prob = max(0.0, min(1.0, prob))
            except (IndexError, ValueError):
                last_original = "[错误]"
                last_new = "用法: :p 0.8"
            continue

        last_original = raw
        last_new = leet_name(raw, prob)
