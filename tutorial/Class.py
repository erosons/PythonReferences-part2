from collections import namedtuple


class Samson:
    def __init__(self, name):
        self.name = name
        self.name = name+"@"+"gmail.com"


class prosper(Samson):
    def __init__(self, color):
        self.color = color


class Krosper:
    def __init__(self, **traits):
        self.traits = traits

    def identity(self):
        print(f"I am Samson's son with {self.traits}")


class Empty:
    pass     # Is a statement you define when you have nothing to pass to the class, the class cannot be left empty without a method


profile = Krosper(color="brown", intelligence="brillant", height=7)
profile.identity()

# validating if the object is an instance of the class
print(isinstance(profile, Krosper))


class Father():
    # this class attribute is accessible to all the instances and Class its self
    mainattr = "two eye"

    def __init__(self, heights, eyecolor):
        # both attrs argument will only be accessible within an instance of the class where it is called on
        self.heights = heights
        self.eyecolor = eyecolor

    def charac(self):
        print(
            f"I am the father of prosper with a height:{self.heights}ft and {self.eyecolor} eyeball")


parent = Father(6, "brown")
parent.charac()

guardian = Father(7, "black")
guardian.eyecolor = "cyan"
guardian.heights = 16
guardian.charac()
parent.charac()

# Calling the class attributes acrosss all the instances and the Class itself
print(guardian.mainattr)
print(parent.mainattr)
print(Father.mainattr)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# Converting to string

    def __str__(self):
        return f"Point({self.x}.{self.y})"
# Comparing instance equality

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
# Comparing instance greater than or less than

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

# Performig addition oprations with instances of a class
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


def draw(self):
    print(f"Point({self.x}.{self.y})")


point = Point(1, 2)
other = Point(1, 2)
# Comparing instances equality
print(point == other)

# Comparing instance greater than or less than
grt = Point(10, 20)
grt1 = Point(1, 2)
print(grt > grt1)
# adding object instances together
print(grt + grt1)

