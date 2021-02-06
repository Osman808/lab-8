#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

# В списке, состоящем из вещественных элементов, вычислить:
# 1) произведение отрицательных элементов списка;

if __name__ == '__main__':
    # Ввести список одной строкой.
    a = list(map(float, input().split()))
    # Если список пуст, завершить программу.
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    s = 1
    for i in [i for i in a if i < 0]:
        s *= i

    print(s)
