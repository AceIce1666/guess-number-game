# -*- coding: utf-8 -*-
"""
猜数字小游戏
电脑随机想一个 1~100 之间的整数，用户输入猜测，
程序提示“大了”“小了”，直到猜中，并统计猜了几次。
单文件完成，直接运行即可。
"""

import random


def main():
    print("=" * 36)
    print("         猜数字小游戏")
    print("电脑已想好一个 1~100 之间的整数，快来猜吧！")
    print("=" * 36)

    # 电脑随机生成 1~100 的目标数字
    answer = random.randint(1, 100)
    count = 0  # 统计猜测次数

    while True:
        raw = input("请输入你猜的数字（1~100）：").strip()

        # 输入校验：非数字或空输入不计数，提示后重新输入
        if not raw.isdigit():
            print("提示：请输入有效的整数！")
            continue

        guess = int(raw)
        if guess < 1 or guess > 100:
            print("提示：数字必须在 1~100 之间！")
            continue

        # 有效猜测，次数 +1
        count += 1

        if guess > answer:
            print("大了！再试一次。")
        elif guess < answer:
            print("小了！再试一次。")
        else:
            print(f"恭喜你，猜中了！答案就是 {answer}。")
            print(f"你一共猜了 {count} 次。")
            break

    # 双击运行时防止窗口一闪而过
    input("按回车键退出...")


if __name__ == "__main__":
    main()
