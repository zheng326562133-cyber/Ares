#!/usr/bin/env python3
"""一个简单的学猫叫小程序。"""


def meow(times: int = 3) -> None:
    """输出指定次数的猫叫。"""
    for _ in range(times):
        print("喵~")


if __name__ == "__main__":
    meow()
