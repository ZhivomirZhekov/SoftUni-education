class Circle:
    __pi = 3.14

    def __init__(self , diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        perimeter = 2 * Circle.__pi * self.diameter / 2
        return perimeter

    def calculate_area(self):
        circle_area = Circle.__pi * (self.diameter / 2) ** 2
        return circle_area

    def calculate_area_of_sector(self , angle):
        result = (angle / 360) * Circle.__pi * (self.diameter / 2) ** 2
        return result


# •	calculate_circumference() - returns the circumference of the circle
# •	calculate_area() - returns the area of the circle
# •	calculate_area_of_sector(angle) - gives the central angle in degrees, returns the area that fills the sector
# Notes: Search the formulas on the internet. Name your methods and variables exactly as in the description! Submit only the class. Test your class before submitting it!
circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
