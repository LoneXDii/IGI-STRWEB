def task2():
    curr_sum = 0
    while curr_sum < 100:
        try:
            x = int(input("Enter integer number:\n"))
        except:
            print("Not an integer number, try again")
            continue
        curr_sum += x
        print("Current sum is ", curr_sum)
    return
