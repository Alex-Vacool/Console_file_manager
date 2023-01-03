#В модуле написать тесты для встроенных функций filter, map, sorted,
# а также для функций из библиотеки math: pi, sqrt, pow, hypot.
# Чем больше тестов на каждую функцию - тем лучше

import math as m

assert m.pi == 3.141592653589793
assert m.sqrt(9) == 3
assert m.sqrt(25) == 5
assert m.pow(2, 3) == 8
assert m.pow(10, 2) == 100
assert m.hypot(3, 4) == 5.0
assert m.hypot(6, 6) == 8.48528137423857