# ADVENT OF CODE
# https://adventofcode.com/2021/day/2
from typing import Iterable


def load_data(filename):
    with open(filename) as f:
        for line in f:
            cmd, units = line.strip().split(" ")
            yield cmd, int(units)


# data = list(load_data('sample.txt'))
# assert len(data) == 6
# assert data[0] == ('forward', 5)
# assert data[-1] == ('forward', 2)


def parser(data: Iterable[tuple[str, int]]):
    hpos, depth = 0, 0
    for movement in data:
        match movement:
            case 'forward', units:
                hpos += units
            case 'down', units:
                depth += units
            case 'up', units:
                depth -= units
            case _:
                raise ValueError('Unknown command')
    return hpos, depth


def solution1(data: Iterable[tuple[str, int]]):
    hpos, depth = parser(data)
    return hpos * depth


assert solution1(load_data('sample.txt')) == 150
print(solution1(load_data('input-sdelquin.txt')))
