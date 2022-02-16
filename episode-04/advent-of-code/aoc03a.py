# ADVENT OF CODE
# https://adventofcode.com/2021/day/3

from collections import Counter
from typing import Iterable, List


def load_data(filename: str) -> List[str]:
    with open(filename) as f:
        return [line.strip() for line in f]


def solution1(lines: List[str]) -> int:
    counters = []
    for line in zip(*lines):
        counter = Counter("".join(line))
        counters.append(counter)
    gamma_rate_tmp = epsilon_rate_tmp = ""
    for counter in counters:
        gamma_rate_tmp += counter.most_common()[0][0]
        epsilon_rate_tmp += counter.most_common()[-1][0]
    gamma_rate = int(gamma_rate_tmp, 2)
    epsilon_rate = int(epsilon_rate_tmp, 2)
    return gamma_rate * epsilon_rate


def solution2(lines: List[str]) -> int:
    counters = [Counter("".join(line)) for line in zip(*lines)]
    gamma_rate = int("".join(map(lambda c: c.most_common()[0][0], counters)), 2)
    epsilon_rate = int("".join(map(lambda c: c.most_common()[-1][0], counters)), 2)
    return gamma_rate * epsilon_rate


def load_data_iter(filename: str) -> Iterable[str]:
    with open(filename) as f:
        yield from map(str.strip, f)


def solution3(lines: Iterable[str]) -> int:
    counters = [Counter(digit) for digit in next(lines)]
    for line in lines:
        for idx, digit in enumerate(line):
            counters[idx].update(digit)
    gamma_rate = int("".join(map(lambda c: c.most_common()[0][0], counters)), 2)
    epsilon_rate = int("".join(map(lambda c: c.most_common()[-1][0], counters)), 2)
    return gamma_rate * epsilon_rate


assert solution1(load_data("sample.txt")) == 198
assert solution2(load_data("sample.txt")) == 198
assert solution3(load_data_iter("sample.txt")) == 198

print(solution1(load_data("input-asamarin.txt")))
print(solution2(load_data("input-asamarin.txt")))
print(solution3(load_data_iter("input-asamarin.txt")))
