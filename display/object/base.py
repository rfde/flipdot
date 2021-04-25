from abc import ABC
from typing import List

from display.canvas import DisplayCanvas
from display.pixel import Pixel

class DisplayObj(ABC):
	def __init__(self, data : List[List[Pixel]]):
		self.__data = data

	def num_columns(self) -> int:
		return len(self.__data)

	def num_rows(self) -> int:
		return 0 if len(self.__data) == 0 else len(self.__data[0])

	def insert(self, canvas : DisplayCanvas, canvas_x : int = 0, canvas_y : int = 0, off_x : int = 0, off_y : int = 0):
		remaining_cs_columns = self.num_columns() - off_x
		remaining_cs_rows    = self.num_rows() - off_y
		remaining_ct_columns = canvas.num_columns() - canvas_x
		remaining_ct_rows    = canvas.num_rows() - canvas_y

		for column_idx in range(min(remaining_cs_columns, remaining_ct_columns)):
			for row_idx in range(min(remaining_cs_rows, remaining_ct_rows)):
				canvas.set(
					canvas_x + column_idx,
					canvas_y + row_idx,
					self.__data[column_idx+off_x][row_idx+off_y]
				)
