class InputService:
    @staticmethod
    def input_int(text=""):
        while True:
            try:
                x = int(input(text))
                break
            except ValueError:
                print("Incorrect input, not int")
        return x

    @staticmethod
    def input_float(text=""):
        while True:
            try:
                x = float(input(text))
                break
            except ValueError:
                print("Incorrect input, not float")
        return x
