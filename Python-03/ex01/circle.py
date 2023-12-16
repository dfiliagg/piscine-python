class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})" 
        

class Circle:
    def __init__(self, center, r):
        self.center = center
        self.r = r

    def __str__(self):
        return f"Circle of center {self.center} and radius {self.r}"
    

def main():
    center = Point(150,100)
    circle = Circle(center, 75)
    print(circle)

if __name__ == "__main__":
    main()
