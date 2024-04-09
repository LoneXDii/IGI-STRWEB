from Services.FractionalGenerator import FractionalGenerator
from Services.Serilializer import Serializer


class Task1:
    @staticmethod
    def __are_equal(nums):
        i = 0
        for number in nums:
            for other in nums[i + 1:]:
                if number == other:
                    return True
            i += 1
        return False

    @staticmethod
    def __find_max(nums):
        max_num = nums[0]
        for num in nums:
            if num > max_num:
                max_num = num
        return max_num

    @staticmethod
    def task1():
        nums = list()
        while True:
            param = input("Enter:\n1.Enter 10 nums from keyboard\n2.Generate 10 nums\n")
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
        print(f"Your nums:")
        for num in nums:
            print(f"{num}\t")

        if Task1.__are_equal(nums):
            print("There are equal elements in list")
        else:
            print('There are no equal elements in list')

        max_num = Task1.__find_max(nums)
        print("Maximal value is: ", str(max_num))
