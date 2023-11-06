class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, point):
        return (
            (self.x - point.x) ** 2 + (self.y - point.y) ** 2 + (self.z - point.z) ** 2
        ) ** 0.5


class Segment3D:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def length(self):
        return self.point1.distance_to(self.point2)

    def middle(self):
        x = (self.point1.x + self.point2.x) / 2
        y = (self.point1.y + self.point2.y) / 2
        z = (self.point1.z + self.point2.z) / 2
        return Point3D(x, y, z)


# import math
# p1 = Point3D(1, 2, 3)
# p2 = Point3D(2.5, 1, -2)
# s = Segment3D(p1, p2)
# print(math.isclose(s.length(), 5.315072906367325, abs_tol=1e-6))
# m = s.middle()
# print(type(m) == Point3D)
# print(m.x == 1.75)
# print(m.y == 1.5)
# print(m.z == 0.5)
