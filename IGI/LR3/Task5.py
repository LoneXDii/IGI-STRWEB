"""This module contains functions for task 5 in IGI LR3"""
from SequenceInitializer import *

def get_task_sum(lst):
    """This function get list of floats and return sum of elements that stands after absolute minimal element"""
    min_elem = float('inf')
    for elem in lst:
        if abs(elem) < abs(min_elem):
            min_elem = elem
    index = lst.index(min_elem)
    answ = 0
    for i in range(index + 1, len(lst)):
        answ += lst[i]
    return answ


def task5():
    """Function that represents console ui for task 4"""
    while True:
        try:
            size = int(input("Enter list size\n"))
            if size <= 0:
                print("Size cannot be less than 1, try again")
                continue
            break
        except ValueError:
            print("Not an integer value, try again")
    lst = list()
    while True:
        param = input("Enter \n1)Enter list by yourself\n2)Generate list\n")
        if param == "1":
            get_list_console(lst, size)
            break
        elif param == "2":
            for i in generate_float_list(size):
                lst.append(i)
            break
        else:
            print("No such command, try again")

    while True:
        task = input("Enter:\n1)Get count of 0\n2)Get sum of elems after abs min value\n3)Print list\n4)Finish\n")
        if task == "1":
            print("Count of 0 is", lst.count(0))
        elif task == "2":
            print(get_task_sum(lst))
        elif task == "3":
            print(lst)
        elif task == "4":
            break
        else:
            print("No such function")
    return
