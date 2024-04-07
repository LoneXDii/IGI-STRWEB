from Services.FractionalGenerator import FractionalGenerator
from Entities.Serilializer import Serializer
from Entities.RationalNum import RationalNum


def are_equal(nums):
    i = 0
    for number in nums:
        for other in nums[i + 1:]:
            if number == other:
                return True
        i += 1
    return False


def find_max(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


def task1():
    nums = list()
    while True:
        param = input("Enter:\n1.Enter 10 nums from keyboard\n2.Generate 10 nums")
        if param == '1':
            for num in FractionalGenerator.get_from_console(10):
                nums.append(num)
            break
        elif param == '2':
            for num in FractionalGenerator.generate_random(10):
                nums.append(num)
            break
        else:
            print("Incorrect parameter, try again")

    Serializer.serialize_csv("Task1.csv", nums)
    Serializer.serialize_pickle("Task1.pickle", nums)

    if are_equal(nums):
        print("There are equal elements in list")
    else:
        print('There are no equal elements in list')

    max_num = find_max(nums)
    print("Maximal value is: ", str(max_num))
