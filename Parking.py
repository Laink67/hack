from typing import List

import cv2
import numpy as np

from Car import Car
from Point import Point
from Slot import Slot


class Parking:

    def __init__(self, id, img_path: str, rows: int, columns: int):
        self.id = id
        self.img = cv2.imread(img_path)
        self.rows = rows
        self.columns = columns
        self.width = self.img.shape[1]
        self.height = self.img.shape[0]
        self.matrix = self.calc_matrix()

    # def width(self):
    #     return int(self.img.shape[1])
    #
    # def height(self):
    #     return self.img.shape[0]

    def calc_matrix(self):
        # compute perspective matrix
        input = np.float32([[7, 104], [348, 38], [472, 118], [42, 248]])
        output = np.float32([[0, 0], [self.width - 1, 0], [self.width - 1, self.height - 1], [0, self.height - 1]])

        return cv2.getPerspectiveTransform(input, output)

    def coords_parking(self) -> List[Slot]:
        width_parking = self.width / self.columns
        height_parking = self.height / self.rows

        slots = []
        id = 0
        for row in np.arange(self.rows):
            for column in np.arange(self.columns):
                point_upper_left = Point(column * width_parking, row * height_parking)
                point_lower_right = Point(point_upper_left.x + width_parking, point_upper_left.y + height_parking)
                slots.append(Slot(id, point_upper_left, point_lower_right))
                id += 1

        return slots

    def transform_cars(self, cars: List[Car]) -> List[Point]:
        centers = [car.center() for car in cars]
        new_centers = []

        for point in centers:
            new_point = np.array([point.x, point.y], dtype=np.float32)
            pts = new_point.reshape(-1, 1, 2).astype(np.float32)
            transformed_arr = cv2.perspectiveTransform(pts, self.matrix)

            new_centers.append(Point(transformed_arr[0][0][0], transformed_arr[0][0][1]))

        return new_centers

    def get_slots_occupied(self, cars: List[Car]):
        slots = self.coords_parking()
        transformed_centers = self.transform_cars(cars)

        slots_occupied = []

        # for slot in slots:
        #     for center in transformed_centers:
        #         if slot.check_occupied(center):
        #             slots_occupied.append(True)
        #             break
        #         else:
        #             slots_occupied.append(False)

        for slot in slots:
            res = [slot.check_occupied(center) for center in transformed_centers]
            print(res)
            slots_occupied.append(res)

        return slots_occupied
