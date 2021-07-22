from datetime import datetime
def parametrized_decorator(path):
    def decorator(old_function):
        def new_function(*args, **kwargs):
            return_value = old_function(*args, **kwargs)
            print(f"Идёт запись лога для функции {old_function.__name__}...")
            with open(path, 'a', encoding='utf-8') as f:
                f.write(f'*** Дата выполнения: {datetime.now().strftime(("%d/%m/%Y %H:%M:%S"))}, имя функции:{(str(old_function.__name__))},\n'
                        f'аргументы: позиционные - {args} именнованные - {kwargs}, результат функции: {return_value}\n')
        return new_function
    return decorator

@parametrized_decorator('task2.txt')
def some_function(parametr1):
    y = parametr1
    return str(y * 2)

some_function(2)

@parametrized_decorator('task2.txt')
def some_function2(parametr1=1, parametr2=2):
    result = parametr1 + parametr2
    return result

some_function2(parametr1=1,parametr2=3)
