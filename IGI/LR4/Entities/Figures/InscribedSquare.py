import math
from PIL import Image, ImageDraw, ImageFont
from Entities.Figures.ShapeColor import ShapeColor
from Entities.Figures.Shape import Shape


class InscribedSquare(Shape):
    def __init__(self, r, color: ShapeColor, text=""):
        self.__r = r
        self.__color = color
        self.__square_side = math.sqrt(2) * r
        self.__text = text
        self.__image = Image.new('RGB', (10, 10), 'white')

    def get_area(self):
        return self.__square_side ** 2

    def __str__(self):
        return '{0} shape, color: {1}, size: {2}, area: {3}'.format(self.__class__.__name__, self.__color,
                                                                    self.__square_side, self.get_area())

    def draw(self):
        image = Image.new('RGB', (2 * (self.__r + 10), 2 * (self.__r + 10)), 'white')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('OpenSans-Regular.ttf', size=14)

        draw.ellipse((10, 10, 2 * self.__r + 10, 2 * self.__r + 10), fill="white", outline='black', width=5)
        center = self.__r + 10
        sq_sp = center - self.__square_side/2
        sq_ep = center + self.__square_side/2
        draw.rectangle((sq_sp, sq_sp, sq_ep, sq_ep), fill=self.__color.color, outline='black')
        draw.text((center - 50, center - 50), self.__text, font=font, fill='black')

        image.show()
        self.__image = image

    def save(self):
        self.__image.save('Task4.jpg')
