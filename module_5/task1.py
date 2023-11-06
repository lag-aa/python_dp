class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, point):
        return (
            (self.x - point.x) ** 2 + (self.y - point.y) ** 2 + (self.z - point.z) ** 2
        ) ** 0.5

# import math
# print(Point3D(0, 0, 0).distance_to(Point3D(0, 0, 0)) == 0)
# p1 = Point3D(1, 2, 3)
# print(p1.x == 1)
# print(p1.y == 2)
# print(p1.z == 3)
# p2 = Point3D(2.5, 1, -2)
# print(math.isclose(p1.distance_to(p2), 5.315072906367325, abs_tol=1e-6))
# p1 = Point3D(-10.3, 2.58, 123.89)
# p2 = Point3D(11.73, -8.91, 12.58)
# print(math.isclose(p1.distance_to(p2), 114.04936255849921, abs_tol=1e-6))