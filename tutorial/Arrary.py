from array import array
x = 10
y = 11

x, y = y, x
print("x:", x)
print("y:", y)


mylist = [1, 2, 3, 4]
# the i-stands for integer, and this type determines what kind of iterable type you can pass
ArrayNumb = array("i", mylist)
print(ArrayNumb)
ArrayNumb.append(5)
ArrayNumb[1] = 10
print(ArrayNumb)
