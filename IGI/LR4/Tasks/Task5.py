from Entities.Matrix import Matrix
from Services.InputService import InputService
import numpy as np


class Task5:
    @staticmethod
    def task5():
        print("Enter n, m - size of matrix:")
        while True:
            try:
                n = InputService.input_int()
                m = InputService.input_int()
                matrix = Matrix(np.random.randint(100, size=(n, m)))
                break
            except ValueError:
                print("Incorrect size, try again")

        print(f"Your matrix is:\n{matrix}\n")

        matrix.rebuild_matrix()
        print(f"Your rebuilded matrix is:\n{matrix}\n")

        print(f"Main diagonal of your matrix: {matrix.get_main_diagonal()}\n")
        print("Median of main diagonal of your matrix:")
        print(f"Numpy: {matrix.get_median_numpy()}")
        print(f"My func: {matrix.get_median()}")
