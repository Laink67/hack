from scipy.spatial import distance
import numpy as np


class ParkingTest:
    places = 20

    def __init__(self, box_parking, cars):
        self.box_parking = box_parking
        self.cars = cars
        self.centers_cars = [self.center(box) for box in cars]
        self.centers_parking = [self.center(box) for box in box_parking]
        self.compare_dist = self.get_compare_dist()
        # self.occupied_parking = [self.compare_dist > ]

    def get_occupied(self):
        res = []
        for center in self.centers_parking:
            for ca in self.centers_cars:
                if self.compare_dist > distance.euclidean(center, ca):
                    res.append(self.compare_dist > distance.euclidean(center, ca))
                    break

        return res

    def center(self, box):
        lower_left = (box[0], box[1])
        upper_right = (box[2], box[3])
        center_x = (lower_left[0] + upper_right[0]) / 2
        center_y = (lower_left[1] + upper_right[1]) / 2

        return center_x, center_y

    def get_compare_dist(self):
        current_parking = self.box_parking[0]
        center = self.centers_parking[0]
        upper_right = (current_parking[2], current_parking[3])

        return distance.euclidean(upper_right, center)
