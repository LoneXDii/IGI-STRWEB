from Tasks.Task1 import Task1
from Tasks.Task2 import Task2
from Tasks.Task3 import Task3
from Tasks.Task4 import Task4
from Tasks.Task5 import Task5

#Pavlovich Vladislav group 253505
#Variant 15
#IGI LR 4

if __name__ == '__main__':
    while True:
        task = input("Enter:\n1)Task 1\n2)Task 2\n3)Task 3\n4)Task 4\n5)Task 5\n6)Finish program\n")
        if task == "1":
            Task1.task1()
        elif task == "2":
            Task2.task2()
        elif task == "3":
            Task3.task3()
        elif task == "4":
            Task4.task4()
        elif task == "5":
            Task5.task5()
        elif task == "6":
            break
        else:
            print("No such task")
