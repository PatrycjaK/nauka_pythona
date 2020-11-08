def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    return 0


if __name__ == '__main__':
    c = calculator(1, 2, '+')
    print(c)
    d = calculator(100, 20, '-')
    print(d)
    e = calculator(5, 4, '*')
    print(e)
    f = calculator(100, 20, '/')
    print(f)
