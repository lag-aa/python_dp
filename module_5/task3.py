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

    def cos_to(self, segment):
        vectorA = (
            self.point1.x - self.point2.x,
            self.point1.y - self.point2.y,
            self.point1.z - self.point2.z,
        )
        vectorB = (
            segment.point1.x - segment.point2.x,
            segment.point1.y - segment.point2.y,
            segment.point1.z - segment.point2.z,
        )
        numerator = (
            vectorA[0] * vectorB[0] + vectorA[1] * vectorB[1] + vectorA[2] * vectorB[2]
        )

        denominator = (vectorA[0] ** 2 + vectorA[1] ** 2 + vectorA[2] ** 2) ** 0.5 * (
            vectorB[0] ** 2 + vectorB[1] ** 2 + vectorB[2] ** 2
        ) ** 0.5

        return abs(numerator / denominator)


# import math
# p1 = Point3D(1, 2, 3)
# p2 = Point3D(2.5, 1, -2)
# s = Segment3D(p1, p2)
# s2 = Segment3D(p2, p1)
# print(math.isclose(s.cos_to(s2), 1, abs_tol=1e-6))
# print(math.isclose(s.cos_to(s), 1, abs_tol=1e-6))
# o = Point3D(0, 0, 0)
# s1 = Segment3D(o, Point3D(3, 0, 0))
# s2 = Segment3D(o, Point3D(0, 2, 0))
# print(math.isclose(s1.cos_to(s2), 0, abs_tol=1e-6))
# s1 = Segment3D(Point3D(0, 0, 0), Point3D(1, 2, 3))
# s2 = Segment3D(Point3D(0, 0, 0), Point3D(1, 0, 0))
# print(math.isclose(s1.cos_to(s2), 0.2672612419124244, abs_tol=1e-6))
