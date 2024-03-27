"""This module contains functions for task 2 in IGI LR3"""

def task2():
    """Main function for task 2, represents all logic of this task"""
    curr_sum = 0
    while curr_sum < 100:
        try:
            x = int(input("Enter integer number:\n"))
        except ValueError:
            print("Not an integer number, try again")
            continue
        curr_sum += x
        print("Current sum is ", curr_sum)
    return
