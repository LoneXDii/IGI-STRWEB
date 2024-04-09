class InputService:
    @staticmethod
    def input_int():
        while True:
            try:
                x = int(input())
                break
            except ValueError:
                print("Incorrect input, try again")
        return x

    @staticmethod
    def input_float():
        while True:
            try:
                x = float(input())
                break
            except ValueError:
                print("Incorrect input, try again")
        return x
