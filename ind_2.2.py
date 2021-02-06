#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

# В списке, состоящем из вещественных элементов, вычислить:
# 2) сумму положительных элементов списка, расположенных до
# максимального элемента.

if __name__ == '__main__':
    # Ввести список одной строкой.
    a = list(map(float, input().split()))
    # Если список пуст, завершить программу.
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    print(sum([i for i in a[:a.index(max(a))] if i > 0]))
