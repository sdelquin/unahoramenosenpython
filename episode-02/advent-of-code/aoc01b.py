import itertools
from typing import Iterable


def load_data(filename: str) -> Iterable[int]:
    with open(filename, 'r') as f:
        for item in f.readlines():
            yield (int(item.strip()))


data = list(load_data('sample.txt'))
assert len(data) == 10
assert data[0] == 199
assert data[1] == 200
assert data[9] == 263


def solution2(data: Iterable[int]) -> int:
    iter1, iter2 = itertools.tee(data)
    # avanzamos un elemento el segundo iterador
    next(iter2)
    counter = 0
    for value1, value2 in zip(iter1, iter2):
        if value2 > value1:
            counter += 1
    return counter


def acc_slide(data: Iterable[int]) -> Iterable[int]:
    iter1, iter2, iter3 = itertools.tee(data, 3)
    next(iter2)
    next(iter3)
    next(iter3)
    for values in zip(iter1, iter2, iter3):
        yield sum(values)


def check(solution):
    assert solution('sample.txt') == 7
    assert solution('input-jileon.txt') == 1709
    assert solution('input-sdelquin.txt') == 1681


print(solution2(acc_slide(load_data('input-sdelquin.txt'))))
