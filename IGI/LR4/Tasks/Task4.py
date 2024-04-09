from Entities.Figures.InscribedSquare import InscribedSquare
from Entities.Figures.ShapeColor import ShapeColor


class Task4:
    @staticmethod
    def task4():
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
