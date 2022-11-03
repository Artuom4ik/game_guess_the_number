import random

print('Привет, мир!')
name = input('Как вас зовут? ')
print('Хорошо', name)
print('Это игра отгадай число. Я загадаю число от 1 до 10. Попробуй отгадай.')
print('У вас будет 5 попыток ')
input('Начнём? Нажмите Enter для старта игры')
secret_number = random.randint(1, 10)
attempts = 5
while attempts > 0:
    print(name, 'У вас осталось попыток', attempts)
    user_number = input('Введите число ')
    user_number = int(user_number)
    if secret_number > user_number:
        print(name, 'Загаданное число больше')
    if secret_number < user_number:
        print(name, 'Загаданное число меньше')
    if secret_number == user_number:
        print('Поздровляю', name, 'Вы отгадали число')
        break
    attempts = attempts - 1
    if attempts < 1:
        print(name, 'Вы проиграли. У вас закончились попытки.')
        print('Секретное число было', secret_number)


