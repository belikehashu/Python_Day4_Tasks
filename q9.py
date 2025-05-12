class Shape:
    def area(self):
        pass

    def perameter(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

    def perameter(self):
        return 2 * (self.l + self.w)

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

    def perameter(self):
        return 2 * 3.14 * self.r


choice = input("Choose shape circle or rectangle: ")

if choice == "circle" or "Circle":
    radius = float(input("Enter radius: "))
    c = Circle(radius)
    print("Area:", c.area())
    print("Perameter:", c.perameter())
elif choice == "rectangle" or "Rectangle":
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    r = Rectangle(l, w)
    print("Area:", r.area())
    print("Perameter:", r.perameter())
