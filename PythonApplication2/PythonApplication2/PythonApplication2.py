d = {1: 'Python', 2: 'python', 3: 'lampa', 4: 'lampochka', 5: 'obama', 6: 'abema', }
a = ' ';
b = ' ';
c = ' ';

while a != d[1] and a != d[2]:
    a = input('Sho my uchim? ')
    if a == d[1] or a == d[2]:
        print('Molodec')
    else:
        print('Staeraysyz')

while b != d[3] and b != d[4]:
    b = input('Sho my uchim? ')
    if b == d[3] or b == d[4]:
        print('Molodec')
    else:
        print('Staeraysyz')

while c != d[5] and c != d[6]:
    c = input('Sho my uchim? ')
    if c == d[5] or c == d[6]:
        print('Molodec')
    else:
        print('Staeraysyz')
