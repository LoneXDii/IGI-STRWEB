from Entities.ExpCalculator import ExpCalculator


class Task3:
    @staticmethod
    def task3():
        calculator = ExpCalculator()
        while True:
            try:
                x = float(input("Enter argument x:\n"))
                eps = float(input("Enter calculation accuracy eps:\n"))
                break
            except ValueError:
                print("Incorrect input, try again")

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
