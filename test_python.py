#В модуле написать тесты для встроенных функций filter, map, sorted,
# а также для функций из библиотеки math: pi, sqrt, pow, hypot.
# Чем больше тестов на каждую функцию - тем лучше

import math as m

#########################################################
numbers = [10, 15, 21, 33, 42, 55]
#########################################################
mapped_numbers = list(map(lambda x: x * 2 + 3, numbers))
print(mapped_numbers)
#########################################################
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)
#########################################################
assert mapped_numbers == [23, 33, 45, 69, 87, 113]
assert sorted_numbers == [55, 42, 33, 21, 15, 10]
#########################################################
def test_pi():
    assert m.pi == 3.141592653589793
def test_sqrt():
    assert m.sqrt(9) == 3
def test_sqrt2():
    assert m.sqrt(25) == 5
def test_pow():
    assert m.pow(2, 3) == 8
def test_pow2():
    assert m.pow(10, 2) == 100
def test_hypot():
    assert m.hypot(3, 4) == 5.0
def test_hypot2():
    assert m.hypot(6, 6) == 8.48528137423857