from abc import ABC, abstractmethod

from display.canvas import DisplayCanvas

class DisplayDevice(ABC):
	def __init__(self, columns : int, rows : int, canvas : DisplayCanvas):
		self._columns : int = columns
		self._rows : int = rows
		self._canvas : DisplayCanvas = canvas
		assert(self._canvas.num_rows() == rows and self._canvas.num_columns() == columns) 

	@abstractmethod
	def refresh(self):
		pass