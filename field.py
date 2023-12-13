import numpy as np

from enum import IntEnum


class CellColor(IntEnum):
    BLACK: int = 0
    WHITE: int = 1


class Field:
    def __init__(self, width: int, height: int):
        self.area = np.full((width, height), CellColor.WHITE, dtype=np.uint8)

    def change_color_on_cell(self, cell_x_pos: int, cell_y_pos: int):
        match self.area[cell_x_pos][cell_y_pos]:
            case CellColor.WHITE:
                self.area[cell_x_pos][cell_y_pos] = CellColor.BLACK
            case CellColor.BLACK:
                self.area[cell_x_pos][cell_y_pos] = CellColor.WHITE
            case _:
                raise Exception("Unknown color!")

    def is_position_outside_the_area(self, x: int, y: int):
        area_width, area_height = self.area.shape
        return any((
            x < 0, x >= area_width,
            y < 0, y >= area_height
        ))
