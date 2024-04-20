from Tasks.Task4.Figures.InscribedSquare import InscribedSquare
from Tasks.Task4.Figures.ShapeColor import ShapeColor
from Tasks.Task import Task


class Task4(Task):
    @staticmethod
    def solve():
        while True:
            try:
                r = int(input("Enter R\n"))
                color = input("Enter color\n")
                text = input("Enter text\n")
                s_color = ShapeColor(color)
                square = InscribedSquare(r, s_color, text)
                square.draw()
                square.save()
                print(str(square))
                break
            except ValueError:
                print('Incorrect input\n')
