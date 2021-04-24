from __future__ import annotations # type annotations for the current class
from typing import List
from enum import Enum

class Pixel(Enum):
	DARK  = 0
	LIGHT = 1

class DisplayContent:
	def __init__(self, columns : int, rows : int, data : List[List[Pixel]]=None):
		assert(columns > 0 and rows > 0)
		if data:
			assert(columns == len(data) and rows == len(data[0]))
			self.__data = data.copy()
		else:
			self.__data : List[List[Pixel]] = [[Pixel.DARK for y in range(rows)] for x in range(columns)]

	def num_columns(self) -> int:
		return len(self.__data)
	
	def num_rows(self) -> int:
		return len(self.__data[0])

	def set(self, column : int, row : int, value : Pixel) -> None:
		self.__data[column][row] = value

	def set_all(self, value : Pixel) -> None:
		for column in self.__data:
			for row_idx in range(len(column)):
				column[row_idx] = value

	def get(self, column : int, row : int) -> Pixel:
		return self.__data[column][row]

	def get_column_vector(self, column : int) -> List[Pixel]:
		# note: returns reference to column vector, not a copy
		return self.__data[column]

	def set_column_vector(self, column : int, vector : List[Pixel]) -> None:
		# note: vector is not copied, the caller may keep a reference
		self.__data[column] = vector

	def reverse_columns(self) -> None:
		self.__data = self.__data[::-1]

	def reverse_rows(self) -> None:
		for column_idx in range(self.num_columns()):
			self.__data[column_idx] = self.__data[column_idx][::-1]

	def rotate_180(self) -> None:
		self.reverse_columns()
		self.reverse_rows()

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
		return DisplayContent(self.num_columns(), self.num_rows(), self.__data)