def get_list():
    while True:
        try:
            size = int(input("Enter size of list"))
            break
        except:
            print("Not an integer number, try again")
    lst = list()
    for i in range(size):
        while True:
            try:
                lst.append(float(input("Enter element of list")))
                break
            except:
                print("Not a float number, try again")
    return lst

def get_task_sum(lst):
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
    lst = get_list()
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
