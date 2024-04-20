from Tasks.MyMixin import MyMixin


class RationalNum(MyMixin):

    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError
        self.num = {'numerator': numerator, 'denominator': denominator}

    def value(self):
        return self.num

    @property
    def numerator(self):
        return self.num.get('numerator')

    @property
    def denominator(self):
        return self.num.get('denominator')

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __ne__(self, other):
        return self.numerator * other.denominator != self.denominator * other.numerator

    def __lt__(self, other):
        res = (self.numerator * other.denominator - self.denominator * other.numerator)
        return res / (self.denominator * other.denominator) < 0

    def __gt__(self, other):
        res = (self.numerator * other.denominator - self.denominator * other.numerator)
        return res / (self.denominator * other.denominator) > 0

    def __le__(self, other):
        res = (self.numerator * other.denominator - self.denominator * other.numerator)
        return res / (self.denominator * other.denominator) <= 0

    def __ge__(self, other):
        res = (self.numerator * other.denominator - self.denominator * other.numerator)
        return res / (self.denominator * other.denominator) >= 0

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
