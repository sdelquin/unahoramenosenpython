# ADVENT OF CODE
# https://adventofcode.com/2021/day/3

from typing import Iterable

import numpy as np


def load_data(filename: str):
    with open(filename) as f:
        for line in f:
            yield ' '.join(c for c in line.strip())


def solution(lines: Iterable[str]):
    data = np.loadtxt(lines, dtype=int)

    # Gamma rate
    rates = data.sum(axis=0) > (data.shape[0] // 2)
    gamma_rate = int(''.join(rates.astype(int).astype(str)), 2)

    # Epsilon rate
    rates = np.invert(rates)
    epsilon_rate = int(''.join(rates.astype(int).astype(str)), 2)

    return gamma_rate * epsilon_rate


assert solution(load_data('sample.txt')) == 198

print(solution(load_data('input-sdelquin.txt')))
