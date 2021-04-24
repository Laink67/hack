from Point import Point


class Slot:

    def __init__(self, id, upper_left: Point, lower_right: Point):
        self.id = id
        self.upper_left = upper_left
        self.lower_right = lower_right
        self.isOccupied = False

    def check_occupied(self, car_center: Point) -> bool:
        self.isOccupied = self.upper_left.x <= car_center.x < self.lower_right.x \
               and self.upper_left.y <= car_center.y < self.lower_right.y

        return self.isOccupied
