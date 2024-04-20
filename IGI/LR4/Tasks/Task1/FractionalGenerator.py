from Tasks.Task1.RationalNum import RationalNum
from Services.InputService import InputService
import random


class FractionalGenerator:
    @staticmethod
    def get_from_console(n: int):
        for i in range(n):
            while True:
                try:
                    a = InputService.input_int("Enter numerator\n")
                    b = InputService.input_int("Enter denominator\n")
                    rn = RationalNum(a, b)
                    print(f"You entered number: {rn}\n")
                    yield rn
                    break
                except ValueError:
                    print("Incorrect input, denominator can't be 0\n")

    @staticmethod
    def generate_random(n: int):
        for i in range(n):
            denominator = random.randint(-100, 100)
            if denominator == 0:
                denominator = 1
            yield RationalNum(random.randint(-100, 100), denominator)
