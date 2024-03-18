from math import exp


def exp_taylor(x, eps):
    true_answ = exp(x)
    answ = 1.0
    n = 1
    factor = 1
    while abs(answ - true_answ) > eps:
        answ += (x ** n) / factor
        n += 1
        factor *= n
        if n > 500:
            print("Reached maximum amount of operations (500)")
            break
    return answ, n, true_answ


def task1():
    while True:
        try:
            x = float(input("Enter argument x:\n"))
            eps = float(input("Enter calculation accuracy eps:\n"))
            break
        except:
            print("Incorrect input, try again")

    answ, n, true_answ = exp_taylor(x, eps)
    print("Math function answer: ", true_answ)
    print("Taylor answer: ", answ)
    print("Count of operations", n)
