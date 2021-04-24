import numpy as np
import cv2

# read input
from typing import List

from Car import Car
from Point import Point
from Slot import Slot

img = cv2.imread("parking.jpg")

# specify desired output size
width = img.shape[1]
height = img.shape[0]

# specify conjugate x,y coordinates (not y,x)
input = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
# input = np.float32([[11, 103], [360, 45], [478, 119], [41, 242]])
output = np.float32([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]])


def coords_parking(rows: int, columns: int):
    width_parking = width / columns
    height_parking = height / rows

    slots = []
    id = 0
    for row in np.arange(rows):
        for column in np.arange(columns):
            point_upper_left = Point(column * width_parking, row * height_parking)
            point_lower_right = Point(point_upper_left.x + width_parking, point_upper_left.y + height_parking)
            slots.append(Slot(id, point_upper_left, point_lower_right))
            id += 1

    return slots


# tmp = coords_parking(2, 5)
# xx = 0

# compute perspective matrix
matrix = cv2.getPerspectiveTransform(input, output)


# def calculate_centers(cars: List[Car]) -> List[Point]:
#     return [car.center() for car in cars]


def transform_cars(cars):
    centers = [car.center() for car in cars]
    new_centers = []

    for point in centers:
        new_point = np.array([point.x, point.y], dtype=np.float32)
        pts = new_point.reshape(-1, 1, 2).astype(np.float32)
        transformed_arr = cv2.perspectiveTransform(pts, matrix)

        new_centers.append(Point(transformed_arr[0][0][0], transformed_arr[0][0][1]))

    return new_centers


def get_slots_occupied(row: int, column: int, cars):
    slots = coords_parking(row, column)
    transformed_centers = transform_cars(cars)

    slots_occupied = []

    for slot in slots:
        for center in transformed_centers:
            slots_occupied.append(slot.check_occupied(center))
            if slots_occupied[-1]:
                break

    return slots_occupied


box_points = np.array([57, 126], dtype=np.float32)
pts = box_points.reshape(-1, 1, 2).astype(np.float32)
print(cv2.perspectiveTransform(pts, matrix)[0][0][0])

# print(matrix.shape)
# print(matrix)

# do perspective transformation setting area outside input to black
imgOutput = cv2.warpPerspective(img, matrix, (width, height), cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT,
                                borderValue=(0, 0, 0))
# print(imgOutput.shape)

# save the warped output
cv2.imwrite("parking_warped.jpg", imgOutput)

# show the result
cv2.imshow("result", imgOutput)
cv2.waitKey(0)
cv2.destroyAllWindows()
