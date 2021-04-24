# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Car import Car
from Parking import Parking
from ParkingTest import ParkingTest
import numpy as np

from Point import Point


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    tmp = (10, 20)

    box_points = [Car(Point(290, 48), Point(350, 92)),
                  Car(Point(325, 49), Point(387, 88)),
                  Car(Point(167, 63), Point(231, 114)),
                  Car(Point(47, 70), Point(102, 124)),
                  Car(Point(400, 97), Point(468, 140)),
                  Car(Point(335, 114), Point(403, 159)),
                  Car(Point(373, 107), Point(445, 150)),
                  Car(Point(292, 127), Point(368, 175)),
                  Car(Point(201, 133), Point(275, 192)),
                  Car(Point(248, 133), Point(323, 182)),
                  Car(Point(145, 148), Point(217, 202)),
                  Car(Point(28, 161), Point(94, 241)),
                  Car(Point(94, 163), Point(170, 228)),
                  Car(Point(383, 17), Point(416, 34)),
                  Car(Point(218, 60), Point(265, 100))]

    parking = Parking(id=1, img_path="parking.jpg", rows=2, columns=10)

    print(f'Occupied slots: {parking.get_slots_occupied(box_points)}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
