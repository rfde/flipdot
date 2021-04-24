from display.base import DisplayBase
from display.content import DisplayContent, Pixel

class DisplaySimulation(DisplayBase):
	def __init__(self, columns : int, rows : int, content : DisplayContent):
		super(DisplaySimulation, self).__init__(columns, rows, content)

	def refresh(self):
		for r in range(self.rows):
			row_str = ""
			for c in range(self.columns):
				row_str += " X" if self.content.get(c, r) == Pixel.LIGHT else " ."
			print(row_str)
		print()