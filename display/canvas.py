from __future__ import annotations # type annotations for the current class

import copy
from typing import List, Tuple, Optional

from display.pixel import Pixel
from display.filter.base import DisplayFilter

class DisplayCanvas:
	def __init__(self, columns : int, rows : int, data : List[List[Pixel]] = None, filters : List[DisplayFilter] = None):
		assert(columns > 0 and rows > 0)
		
		if data:
			assert(columns == len(data) and rows == len(data[0]))
			self.__data : List[List[Pixel]] = data.copy()
		else:
			self.__data = [[Pixel.DARK for y in range(rows)] for x in range(columns)]
		
		if filters:
			self.__filters : List[DisplayFilter] = filters.copy()
		else:
			self.__filters = []

	def num_columns(self) -> int:
		return len(self.__data)
	
	def num_rows(self) -> int:
		return len(self.__data[0])

	def set(self, column : int, row : int, value : Pixel) -> None:
		if (column >= 0 and row >= 0 and column < self.num_columns() and row < self.num_rows()):
			self.__data[column][row] = value

	def set_all(self, value : Pixel) -> None:
		for column_idx in range(self.num_columns()):
			for row_idx in range(self.num_rows()):
				self.set(column_idx, row_idx, value)

	def set_square(self, x : int, y : int, width : int, height : int, value : Pixel) -> None:
		for column_idx in range(x, x + width):
			for row_idx in range(y, y + height):
				self.set(column_idx, row_idx, value)

	def get(self, column : int, row : int, filtered : bool) -> Pixel:
		# apply coordinate filters
		if filtered:
			for f in self.__filters:
				column, row = f.filter_coordinate(column, row)
		assert(column >= 0 and row >= 0 and column < self.num_columns() and row < self.num_rows())

		value = self.__data[column][row] 
		# apply value filters
		if filtered:
			for f in self.__filters:
				value = f.filter_value(value)
		return value

	def get_column_vector(self, column : int, filtered : bool) -> List[Pixel]:
		if filtered:
			result : List[Pixel] = []
			for row_idx in range(self.num_rows()):
				result.append(self.get(column, row_idx, filtered=True))
			return result
		else:
			return self.__data[column].copy()

	
	def add_filter(self, dfilter : DisplayFilter) -> None:
		self.__filters.append(dfilter)

	def clear_filters(self) -> None:
		self.__filters.clear()

	def diff_column_vectors(self, other : Optional[DisplayCanvas]) -> List[Tuple[int, List[Pixel]]]:
		"""
		Compares two DisplayCanvas objects. Returns the column vectors from self that
		differ from those in other. If other is None, return all column vectors.
		"""
		result : List[Tuple[int, List[Pixel]]] = []
		if other is None:
			for column_idx in range(self.num_columns()):
				result.append((column_idx, self.get_column_vector(column_idx, filtered=True)))
		else:
			assert(self.num_columns() == other.num_columns() and self.num_rows() == other.num_rows())
			for column_idx in range(self.num_columns()):
				same = True
				for row_idx in range(self.num_rows()):
					if self.get(column_idx, row_idx, filtered=True) \
							!= other.get(column_idx, row_idx, filtered=True):
						same = False
						break
				if not same:
					result.append((column_idx, self.get_column_vector(column_idx, filtered=True)))
		return result

	def copy(self) -> DisplayCanvas:
		return DisplayCanvas(self.num_columns(), self.num_rows(), copy.deepcopy(self.__data), copy.deepcopy(self.__filters))