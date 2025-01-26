class Areas():
    def __init__(self, radius, height, width):
        self.radi = radius;
        self.heig = height;
        self.wid = width;

    def AreaOfCircle(self):
        return self.radi * self.radi * 3.14;

    def AreaOfRectangle(self):
        return self.heig * self.wid;


r = int(input("Enter the value for Radius of Circle: "))
h = int(input("Enter the value for Height of Rectangle: "))
w = int(input("Enter the value for Width of Rectangle: "))

a = Areas(2, 4, 5)
print("Area of Circle is : ", a.AreaOfCircle())
print("Area of Rectangle is : ", a.AreaOfRectangle())


# Draw Circle:
import matplotlib.pyplot as plt
%matplotlib inline
class Circle(object):

    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

        # Method

    def add_radius(self, r):
        self.radius = self.radius + r
        return (self.radius)

    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

RedCircle = Circle(10, 'red')
dir(RedCircle)
RedCircle.radius
RedCircle.color
RedCircle.radius = 1
RedCircle.radius
RedCircle.drawCircle()

# Use method to change the object attribute radius

print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)

# Create a blue circle with a given radius
BlueCircle = Circle(radius=100)

# Print the object attribute radius
BlueCircle.radius
