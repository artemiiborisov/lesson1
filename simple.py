a = 2
b = 0.5
print(a + b)

name = (input('ВСТАВЬТЕ ВАШЕ ИМЯ'))
b = f'Привет {name}! Как дела?'
print(b)

v = int(input('Введите число от 1 до 10:'))
if 0 < v <= 10:
    print(v + 10)
else:
    print('Надо было ввести от 1 до 10')

print(float('1'))
print(bool(1))
print(bool(''))
print(bool(0))