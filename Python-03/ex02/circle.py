import math
import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"        

class Circle:
    def __init__(self, center, r):
        self.center = Point(center[0], center[1])
        self.r = r

    def __str__(self):
        return f"Circle of center {self.center} and radius {self.r}"

    def contains(self, point):
        x = self.center.x - point.x
        y = self.center.y - point.y
        operation = "(" + str(x) + ")**2" + "+" + "(" + str(y) + ")**2"
        res = math.sqrt(eval(operation))
        if res > self.r:
            return False
        return True

def main():
    if len(sys.argv) != 3:
        print ("Error")
        exit()
    circle = Circle((0,0), 1)
    point = Point(float(sys.argv[1]),float(sys.argv[2])) 
    if circle.contains(point):
        res = f"The Point {point} lies in the Circle of center {circle.center} and radius {circle.r}"
        print(res)
    else:
        res = f"The Point {point} lies out of the Circle of center {circle.center} and radius {circle.r}"
        print(res)

if __name__ == "__main__":
    main()
