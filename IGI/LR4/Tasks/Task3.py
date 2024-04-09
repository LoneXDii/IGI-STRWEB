from Entities.ExpCalculator import ExpCalculator
from Services.InputService import InputService


class Task3:
    @staticmethod
    def task3():
        calculator = ExpCalculator()
        print("Enter argument x:")
        x = InputService.input_float()
        print("Enter calculation accuracy eps:")
        eps = InputService.input_float()

        answ, n, true_answ = calculator.calculate(x, eps)
        print("X: ", x)
        print("Count of operations", n)
        print("Taylor answer: ", answ)
        print("Math function answer: ", true_answ)
        print("Accuracy: ", eps)

        print(f'Data: {calculator.data}')
        print(f'Average: {calculator.get_average()}')
        print(f'Median: {calculator.get_median()}')
        print(f'Mode: {calculator.get_mode()}')
        print(f'Dispersion: {calculator.get_dispersion()}')
        print(f'Average square deviation: {calculator.get_average_square_deviation()}')

        calculator.plot(-2, 2, 0.1, 'plot.png')
