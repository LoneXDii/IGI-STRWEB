#IGI lab3 variant 15
#Pavlovich Vladislav 253505
#Finished at 18.03.24

from Task1 import task1
from Task2 import task2
from Task3 import task3
from Task4 import task4
from Task5 import task5

while True:
    task = input("Enter:\n1)Task 1\n2)Task 2\n3)Task 3\n4)Task 4\n5)Task 5\n6)Finish program\n")
    if task == "1":
        task1()
    elif task == "2":
        task2()
    elif task == "3":
        task3()
    elif task == "4":
        task4()
    elif task == "5":
        task5()
    elif task == "6":
        break
    else:
        print("No such task")
