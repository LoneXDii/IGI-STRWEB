import os

import circle
import square


x = os.environ['PARAM']
param = int(x)

print("Square area = ", square.area(param))
print("Square perimeter = ", square.perimeter(param))
print("Circle area = ", circle.area(param))
print("Circle perimeter = ", circle.perimeter(param))