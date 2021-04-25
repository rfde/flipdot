from abc import ABC, abstractmethod

from display.canvas import DisplayCanvas

class DisplayDevice(ABC):
	def __init__(self, columns : int, rows : int, canvas : DisplayCanvas):
		self.columns : int = columns
		self.rows : int = rows
		self.canvas : DisplayCanvas = canvas
		assert(self.canvas.num_rows() == rows and self.canvas.num_columns() == columns) 

	@abstractmethod
	def refresh(self):
		pass