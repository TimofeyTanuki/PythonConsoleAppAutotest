def lagrange(a, len=4):
    x = int(a**0.5)
    if a == x**2:
        return str(x)
    if len == 1:
        return 0
    while lagrange(a - x**2, len-1) == 0:
        x-=1
        if x <=0:
            return 0
    return str(x) + ' ' + lagrange(a - x**2, len-1)
a = input()
if a.isnumeric():
    print(lagrange(int(a)))
else:
    print('Неверный формат ввода!')