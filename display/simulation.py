from display.base import Display
from display.content import DisplayContent, Pixel

class DisplaySimulation(Display):
	def __init__(self, columns : int, rows : int, content : DisplayContent, filtered : bool = True):
		super(DisplaySimulation, self).__init__(columns, rows, content)
		self.__filtered = filtered

	def refresh(self):
		for r in range(self.rows):
			row_str = ""
			for c in range(self.columns):
				row_str += "\u2588" if self.content.get(c, r, self.__filtered) == Pixel.LIGHT else "."
			print(row_str)
		print()