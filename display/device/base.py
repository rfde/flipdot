from abc import ABC, abstractmethod

from display.canvas import DisplayCanvas

class DisplayDevice(ABC):
	def __init__(self, columns : int, rows : int, canvas : DisplayCanvas):
		self.__columns : int = columns
		self.__rows : int = rows
		self.__canvas : DisplayCanvas = canvas
		assert(self.__canvas.num_rows() == rows and self.__canvas.num_columns() == columns) 

	@abstractmethod
	def refresh(self):
		pass