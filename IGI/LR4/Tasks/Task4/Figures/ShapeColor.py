from Tasks.MyMixin import MyMixin


class ShapeColor(MyMixin):

    def __init__(self, color: str):
        self.__color = color

    def set_color(self, new_color):
        self.__color = new_color

    def get_color(self):
        return self.__color

    def del_color(self):
        del self.__color

    color = property(get_color, set_color, del_color)

    def __str__(self):
        return self.__color
