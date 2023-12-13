import numpy as np
from PIL import Image
from typing import Tuple

from ant import Ant, MovementDirection
from field import Field, CellColor


def main():
    start_x, start_y, start_direction = 512, 512, MovementDirection.UP
    ant: Ant = Ant(start_x, start_y, start_direction)
    width, height = 1024, 1024
    field: Field = Field(width, height)

    next_ant_position: Tuple[int, int] = ant.look_forward_next_position()
    while not field.is_position_outside_the_area(*next_ant_position):
        current_ant_position: Tuple[int, int] = ant.x, ant.y
        field.change_color_on_cell(*current_ant_position)
        ant.move(*next_ant_position)
        next_ant_direction = get_next_direction_by_cell_color(field.area[ant.x][ant.y])
        ant.rotate_direction(next_ant_direction)
        next_ant_position = ant.look_forward_next_position()

    area_for_image: np.ndarray = field.area
    # if your need to reverse result image by vertical - uncomment string down
    # area_for_image = area_for_image[::-1]

    result_image: Image = convert_field_to_image(area_for_image)
    # result_image.show()
    result_image.save(".\\result.png", bitmap_format="png")
    black_points_count_on_area: int = get_black_points_count_on_area(area_for_image)
    print(f"{black_points_count_on_area=}")
    color_numbers, counts = np.unique(area_for_image, return_counts=True)
    print(dict(zip(color_numbers, counts)))


def get_next_direction_by_cell_color(cell_color: CellColor) -> int:
    match cell_color:
        case CellColor.WHITE:
            return MovementDirection.RIGHT
        case CellColor.BLACK:
            return MovementDirection.LEFT
        case _:
            raise Exception("Unknown color!")


def convert_field_to_image(field_area: np.ndarray) -> Image:
    width, height = field_area.shape
    converted_array: np.ndarray = np.zeros((width, height, 3), dtype=np.uint8)

    for i in range(width):
        for j in range(height):
            if field_area[i][j] == CellColor.WHITE:
                converted_array[i][j] = (255, 255, 255)

    image = Image.fromarray(converted_array)
    return image


def get_black_points_count_on_area(field_area: np.ndarray):
    width, height = field_area.shape
    black_points_count: int = 0
    for x in range(width):
        for y in range(height):
            if field_area[x][y] == CellColor.BLACK:
                black_points_count += 1

    return black_points_count


if __name__ == '__main__':
    main()
