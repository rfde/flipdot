from typing import Tuple
from display.filter.base import DisplayFilter
from display.pixel import Pixel

class DisplayFilterRotate180(DisplayFilter):
	def __init__(self, columns : int, rows : int):
		self.__columns = columns
		self.__rows = rows
		super(DisplayFilterRotate180, self).__init__()

	def filter_coordinate(self, column : int, row : int) -> Tuple[int, int]:
		assert(column < self.__columns and row < self.__rows)
		return (
			self.__columns - column - 1,
			self.__rows - row - 1
		)