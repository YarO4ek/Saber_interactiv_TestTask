'''Данным кодом я реализовал калькулятор для двух чисел'''

a = float(input('Введите первое число:'))
b = float(input('Введите второе число:'))
c = input('Введите операцию любую из операций +, -, /, *, mod, pow, div:')
if c == '+':
    print(a + b)
elif c == 'mod':
    if b == 0:
        print("Деление на 0!")
    else:
        print(a % b)
elif c == '-':
    print(a - b)
elif c == '+':
    print(a + b)
elif c == '*':
    print(a * b)
elif c == 'pow':
    print(pow(a, b))
elif c == 'div':
    if b == 0:
        print("Деление на 0!")
    else:
        print(a // b)
elif c == "/":
    if b == 0:
        print("Деление на 0!")
    else:
        print(a / b)