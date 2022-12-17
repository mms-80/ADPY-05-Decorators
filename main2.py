import os
from utils import _logger


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')
    for path in paths:
        if os.path.exists(path):
            os.remove(path)

    @_logger('Logs/log_1.log')
    def hello_world():
        return 'Hello World'

    @_logger('Logs/log_2.log')
    def summator(a, b=0):
        return a + b

    @_logger('Logs/log_3.log')
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'
    summator(4.3, b=2.2)


if __name__ == '__main__':
    test_2()
