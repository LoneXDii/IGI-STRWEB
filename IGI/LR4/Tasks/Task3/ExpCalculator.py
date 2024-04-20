import numpy as np
import matplotlib.pyplot as plt
import math
from Tasks.MyMixin import MyMixin


class ExpCalculator(MyMixin):
    def __init__(self):
        self.__data = np.array([])

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        self.__data = new_data

    def calculate(self, x, eps):
        true_answ = math.exp(x)
        answ = 1.0
        n = 1
        factor = 1
        series_elements = np.array([])
        while abs(answ - true_answ) > eps:
            element = (x ** n) / factor
            answ += element
            series_elements = np.append(series_elements, element)
            n += 1
            factor *= n
            if n > 500:
                print("Reached maximum amount of operations (500)")
                break

        self.data = series_elements
        return answ, n - 1, true_answ

    def plot(self, x_min, x_max, step, path_to_file=None):
        x = np.arange(x_min, x_max, step)

        y_math = [math.exp(val) for val in x]
        y_taylor = [self.calculate(val, 0.01)[0] for val in x]

        plt.plot(x, y_math, color="green")
        plt.plot(x, y_taylor, color="red")
        plt.xlabel('x')
        plt.ylabel('e^x')
        plt.legend(['math.exp', 'taylor series for exp'])

        if path_to_file:
            try:
                plt.savefig(path_to_file)
            except ValueError:
                print("Incorrect path to file\n")

        plt.show()

    def get_average(self):
        return np.average(self.__data)

    def get_median(self):
        return np.median(self.__data)

    def get_mode(self):
        vals, counts = np.unique(self.__data, return_counts=True)
        index = np.argmax(counts)
        return vals[index]

    def get_dispersion(self):
        return np.var(self.__data)

    def get_average_square_deviation(self):
        return np.std(self.__data)
