#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import math

def cpu_heavy_op(value):
    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    print()
    return math.sqrt(value)

items = [cpu_heavy_op(4), cpu_heavy_op(4)**2, cpu_heavy_op(4)**3]
# items = [x := cpu_heavy_op(4), x**2, x**3]
assert items == [2, 4, 8]
print(f"items: {items!r}")
