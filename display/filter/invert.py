from display.filter.base import DisplayFilter
from display.content import Pixel

class DisplayFilterInvert(DisplayFilter):
	def __init__(self):
		super(DisplayFilterInvert, self).__init__()

	def filter_value(self, value : Pixel) -> Pixel:
		return Pixel.DARK if value == Pixel.LIGHT else Pixel.LIGHT