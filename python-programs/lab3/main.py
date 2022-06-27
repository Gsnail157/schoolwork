from fraction import Fraction


def H(n):
    total = Fraction(1, 1)
    for num in range(2, n+1):
        total += Fraction(1, num)
    print(f'H({n})=', end='')
    print(total)
    print(f'H({n})~=', end='')
    print("{:.8f}".format(total.approximate()))


def T(n):
    total = Fraction(1, 2) ** 0
    for num in range(1, n+1):
        total += Fraction(1, 2) ** (num)
    print(f'T({n})=', end='')
    print(total)
    print(f'T({n})~=', end='')
    print("{:.8f}".format(total.approximate()))


def Z(n):
    total = Fraction(1, 2) ** 0
    for num in range(1, n+1):
        total += (Fraction(1, 2) ** num)
    new = Fraction(1, total.getNum()) * total

    print(f'Z({n})=', end='')
    print(new)
    print(f'Z({n})~=', end='')
    print("{:.8f}".format(new.approximate()))


def R(n, b):
    total = Fraction(1, 1)
    for num in range(2, n+1):
        total += Fraction(1, num) ** b
    print(f'R({n},{b})=', end='')
    print(total)
    print(f'R({n},{b})~=', end='')
    print("{:.8f}".format(total.approximate()))


if __name__ == "__main__":
    print(f'Welcome to Fun with Fractions!')
    while True:
        try:
            num = int(input("Enter Number of iterations (integer>0):\n"))
            if num < 0:
                raise ValueError
            else:
                H(num)
                T(num)
                Z(num)
                R(num, num)
                break
        except ValueError as e:
            print("Bad Input")
