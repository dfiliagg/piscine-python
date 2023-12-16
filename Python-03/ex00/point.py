import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    try:
        point = input("Insert the coordinates of the first point: ")
        i = 0
        while point[i] != ",":
            i += 1
        x = float(point[:i])
        y = float(point[i+1])
        point1 = Point(x,y)
        point = input("Insert the coordinates of the second point: ")
        i = 0
        while point[i] != ",":
            i += 1
        x = float(point[:i])
        y = float(point[i+1])
        point2 = Point(x,y)
        x = point1.x - point2.x
        y = point1.y - point2.y
        operation = "(" + str(x) + ")**2" + "+" + "(" + str(y) + ")**2"
        res = eval(operation)
        print("Their distance is:", math.sqrt(res))
    except:
        print("Error")

if __name__ == "__main__":
    main()
