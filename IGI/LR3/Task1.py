"""This module contains functions for task 1 in IGI LR3"""

from math import exp

def exp_taylor(x, eps):
    """Main function of task1
    x - float value, argument of epx function
    eps - float value, calculation accuracy
    return taylor series result, count of operations, value of embedded python function"""
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
    """Function that represents console ui for task 1"""
    while True:
        try:
            x = float(input("Enter argument x:\n"))
            eps = float(input("Enter calculation accuracy eps:\n"))
            break
        except ValueError:
            print("Incorrect input, try again")

    answ, n, true_answ = exp_taylor(x, eps)
    print("Math function answer: ", true_answ)
    print("Taylor answer: ", answ)
    print("Count of operations", n)
