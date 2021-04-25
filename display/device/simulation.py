from display.device.base import DisplayDevice
from display.canvas import DisplayCanvas
from display.pixel import Pixel

class DisplayDeviceSimulation(DisplayDevice):
	def __init__(self, columns : int, rows : int, canvas : DisplayCanvas, filtered : bool = True):
		super(DisplayDeviceSimulation, self).__init__(columns, rows, canvas)
		self.__filtered : bool = filtered

	def refresh(self):
		for r in range(self.rows):
			row_str = ""
			for c in range(self.columns):
				row_str += "\u2588" if self.__canvas.get(c, r, self.__filtered) == Pixel.LIGHT else "."
			print(row_str)
		print()