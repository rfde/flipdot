from abc import ABC, abstractmethod

from display.content import DisplayContent

class DisplayBase(ABC):
	def __init__(self, columns : int, rows : int, content : DisplayContent):
		self.columns : int = columns
		self.rows : int = rows
		self.content : DisplayContent = content
		assert(self.content.num_rows() == rows and self.content.num_columns() == columns) 

	@abstractmethod
	def refresh(self):
		pass