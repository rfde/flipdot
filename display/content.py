from __future__ import annotations # type annotations for the current class
from typing import List
from enum import Enum

class Pixel(Enum):
	DARK  = 0
	LIGHT = 1

class DisplayContent:
	def __init__(self, columns : int, rows : int, data : List[List[Pixel]] = None, filters : List[DisplayFilter] = None):
		assert(columns > 0 and rows > 0)
		
		if data:
			assert(columns == len(data) and rows == len(data[0]))
			self.__data = data.copy()
		else:
			self.__data : List[List[Pixel]] = [[Pixel.DARK for y in range(rows)] for x in range(columns)]
		
		if filters:
			self.__filters = filters.copy()
		else:
			self.__filters : List[DisplayFilter] = []

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
		# apply coordinate filters
		if filtered:
			for f in self.__filters:
				column, _ = f.filter_coordinate(column, 0)
		# apply value filters
		column_vector = self.__data[column].copy()
		if filtered:
			for row_idx in range(len(column_vector)):
				for f in filters:
					column_vector[row_idx] = f.filter_value(column_vector[row_idx])
		return column_vector

	
	def add_filter(self, dfilter : DisplayFilter) -> None:
		self.__filters.append(dfilter)

	def clear_filters(self) -> None:
		self.__filters.clear()

	# def reverse_columns(self) -> None:
	# 	self.__data = self.__data[::-1]

	# def reverse_rows(self) -> None:
	# 	for column_idx in range(self.num_columns()):
	# 		self.__data[column_idx] = self.__data[column_idx][::-1]

	# def rotate_180(self) -> None:
	# 	self.reverse_columns()
	# 	self.reverse_rows()

	# def invert(self, x : int = 0, y : int = 0, width : int = None, height : int = None) -> None:
	# 	if width is None:
	# 		width = self.num_columns()
	# 	if height is None:
	# 		height = self.num_rows()
	# 	for column_idx in range(x, min(x+width, self.num_columns())):
	# 		for row_idx in range(y, min(y+height, self.num_rows())):
	# 			self.__data[column_idx][row_idx] = \
	# 				Pixel.LIGHT if self.__data[column_idx][row_idx] == Pixel.DARK else Pixel.DARK

	def diff_column_vectors(self, other : DisplayContent) -> List[Tuple[int, List[Pixel]]]:
		"""
		Compares two DisplayContent objects. Returns the column vectors from self that
		differ from those in other.
		
		:param      other:  The other DIsplayContent
		
		:returns:   A list of tuples that represent differing columns; each tuple contains
		            column index and contents of that column from self.
		"""
		assert(self.num_columns() == other.num_columns() and self.num_rows() == other.num_rows())
		result : List[Tuple[int, List[Pixel]]] = []
		for column_idx in range(self.num_columns()):
			same = True
			for row_idx in range(self.num_rows()):
				if self.get(column_idx, row_idx) != other.get(column_idx, row_idx):
					same = False
					break
			if not same:
				result.append((column_idx, self.get_column_vector(column_idx)))
		return result

	def copy(self) -> DisplayContent:
		return DisplayContent(self.num_columns(), self.num_rows(), self.__data, self.__filters)