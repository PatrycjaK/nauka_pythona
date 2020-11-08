def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b

if __name__ == '__main__':
    c = calculator(1, 2, '+')
    print(c)
    d = calculator(100, 20, '-')
    print(d)
