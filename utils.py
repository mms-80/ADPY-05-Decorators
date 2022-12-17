from datetime import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        date_time = datetime.now()
        func_name = old_function.__name__
        result = old_function(*args, **kwargs)
        with open('Logs/main.log', 'a', encoding='cp1251') as file:
            file.write(f'Дата/время: {date_time}\n'
                       f'Имя функции: {func_name}\n'
                       f'Аргументы: {args, kwargs}\n'
                       f'Результат: {result}\n'
                       f'{"*"*50}\n')

        return result

    return new_function



def _logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            date_time = datetime.now()
            func_name = old_function.__name__
            result = old_function(*args, **kwargs)
            with open(f'{path}', 'a', encoding='utf-8') as file:
                file.write(f'Дата/время: {date_time}\n'
                           f'Имя функции: {func_name}\n'
                           f'Аргументы: {args, kwargs}\n'
                           f'Результат: {result}\n'
                           f'{"*" * 50}\n')

            return result
        return new_function
    return __logger