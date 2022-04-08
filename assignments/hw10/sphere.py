
import math
class Sphere:
    radius = 4

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        return math.pi * self.radius**2

    def volume(self):
        return (4/3) * math.pi * self.radius**3




