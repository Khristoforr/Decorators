from datetime import datetime
import requests
TOKEN = 2619421814940190

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

@parametrized_decorator('task3.txt')
def get_superhero_id(name):
    resp = requests.get(f'https://superheroapi.com/api/{TOKEN}/search/{name}').json()['results']
    for hero in resp:
      return hero['id']

print(get_superhero_id('Hulk'))