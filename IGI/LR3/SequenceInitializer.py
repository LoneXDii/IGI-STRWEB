"""This module contains function for sequence initialisation"""
import random

def get_list_console(n):
    """This function get list of floats from console
    seq - sequence for initializing
    n - seq size
    return initialized seq"""
    for i in range(n):
        while True:
            try:
                yield float(input("Enter element of list\n"))
                break
            except ValueError:
                print("Not a float number, try again")

def generate_float_list(n):
    """This function generates list of floats
    n - seq size
    return initialized seq"""
    gen = (random.random() * random.randint(0, 100) for i in range(n))
    for i in range(n):
        yield next(gen)
