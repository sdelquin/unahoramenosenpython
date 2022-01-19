import itertools


def load_data(filename):
    with open(filename, 'r') as f:
        for item in f.readlines():
            yield (int(item.strip()))


# for i in load_data('sample.txt'):
#     # llamada implícita a next() -> siguiente elemento del generador
#     print(i)

data = list(load_data('sample.txt'))
assert len(data) == 10
assert data[0] == 199
assert data[1] == 200
assert data[9] == 263


def solution1(filename):
    data = list(load_data(filename))
    num_data = len(data)  # necesitamos saber el número total de elementos
    counter = 0
    for i in range(0, num_data - 1):
        a = data[i]
        b = data[i + 1]
        if b > a:
            counter += 1
    return counter


def solution2(filename):
    '''Esta solución está basada en iteradores'''
    iter1, iter2 = itertools.tee(load_data(filename))
    # avanzamos un elemento el segundo iterador
    next(iter2)
    counter = 0
    for value1, value2 in zip(iter1, iter2):
        if value2 > value1:
            counter += 1
    return counter


def solution3(filename):
    '''Esta solución está basada en listas por comprensión'''
    iter1, iter2 = itertools.tee(load_data(filename))
    next(iter2)
    return sum(1 if v2 > v1 else 0 for v1, v2 in zip(iter1, iter2))


def solution3b(filename):
    '''Esta solución está basada en listas por comprensión'''
    iter1, iter2 = itertools.tee(load_data(filename))
    next(iter2)
    return sum(v2 > v1 for v1, v2 in zip(iter1, iter2))


def solution4(filename):
    '''Esta solución está basada en los comentarios de Cristian cmaureir'''
    data = list(load_data(filename))
    return sum(1 for i, j in zip(data, data[1:]) if j - i > 0)


def solution5(filename):
    return sum(
        1 for value1, value2 in itertools.pairwise(load_data(filename)) if value2 > value1
    )


def check(solution):
    assert solution('sample.txt') == 7
    assert solution('input-jileon.txt') == 1709
    assert solution('input-sdelquin.txt') == 1681


check(solution1)
check(solution2)
check(solution3)
check(solution4)
check(solution5)
