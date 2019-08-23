from random import uniform, _pi

random_sum = 0


def area_of_crescent():
    for max_darts in range(1, 6):
        number_of_darts = 10 ** max_darts
        between_square_and_circle = 0
        area_of_square = 16
        for i in range(0, number_of_darts):
            x_coordinate = uniform(a=-2, b=2)
            y_coordinate = uniform(a=-2, b=2)
            if x_coordinate ** 2 + y_coordinate ** 2 >= 4 and -2 <= x_coordinate <= 2 and -2 <= y_coordinate <= 2:
                between_square_and_circle += 1
            area_of_object = area_of_square * between_square_and_circle / number_of_darts
        print(f"NumberOfDarts::{number_of_darts}||EstimatedArea::{area_of_object}")


def area_between_circle_and_ellipse():
    for max_darts in range(1, 6):
        minor_axis = 1
        major_axis = 2
        area_of_ellipse = _pi * major_axis * minor_axis
        n_darts = 10 ** max_darts
        number_of_hits = 0
        number_of_misses = 0
        for i in range(0, n_darts):
            x_coord = uniform(a=-2, b=2)
            y_coord = uniform(a=-1, b=1)
            if (x_coord ** 2 + y_coord ** 2 > 1) and (x_coord / 2) ** 2 + (y_coord / 1) ** 2 < 1:
                number_of_hits += 1
            else:
                number_of_misses += 1
            area_obj = area_of_ellipse * number_of_hits / n_darts
            area_of_non = 8 * number_of_misses / n_darts
        yield f"NumberOfDarts::{n_darts}||EstimatedArea::{area_obj}"


if __name__ == '__main__':
    for statement in area_between_circle_and_ellipse():
        print(statement)
