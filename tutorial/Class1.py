from collections import namedtuple
# A better way to deal with classes that has only data and no method.
"""class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y"""

# This is comparism of Objects
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
p3 = Point(x=4, y=3)
p4 = Point(x=1, y=2)
print(p1 == p2)
print(p3 > p4)
