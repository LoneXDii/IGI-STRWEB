from Entities.RationalNum import RationalNum
import random


class FractionalGenerator:

    @staticmethod
    def get_from_console(n: int):
        for i in range(n):
            while True:
                try:
                    a = int(input("Enter numerator"))
                    b = int(input("Enter denominator"))
                    yield RationalNum(a, b)
                    break
                except ValueError:
                    print("Incorrect input, try again")

    @staticmethod
    def generate_random(n: int):
        for i in range(n):
            yield RationalNum(random.randint(-100, 100), random.randint(-100, 100))
