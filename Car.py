from Point import Point


class Car:

    def __init__(self, upper_left: Point, lower_right: Point):
        self.upper_left = upper_left
        self.lower_right = lower_right

    def center(self) -> Point:
        center_x = (self.upper_left.x + self.lower_right.x) / 2
        center_y = (self.upper_left.y + self.lower_right.y) / 2

        return Point(center_x, center_y)
