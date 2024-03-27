"""This module contains function for sequence initialisation"""
import random

def get_list_console(seq, n):
    """This function get list of floats from console
    seq - sequence for initializing
    n - seq size
    return initialized seq"""
    for i in range(n):
        while True:
            try:
                seq.append(float(input("Enter element of list\n")))
                break
            except ValueError:
                print("Not a float number, try again")
    return seq

def generate_float_list(seq, n):
    """This function generates list of floats
    seq - sequence for initializing
    n - seq size
    return initialized seq"""
    gen = (random.random() * random.randint(0, 100) for i in range(n))
    for i in range(n):
        seq.append(next(gen))
    return seq

