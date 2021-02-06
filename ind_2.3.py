#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

# В списке, состоящем из вещественных элементов, вычислить:
# Изменить порядок следования элементов в списке на обратный.

if __name__ == '__main__':
    # Ввести список одной строкой.
    a = list(map(float, input().split()))
    # Если список пуст, завершить программу.
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    a.reverse()
    print(a)
