from typing import List
from PIL import Image

from display.content import Pixel, DisplayContent
from display.object.base import DisplayObj

class DisplayObjImage(DisplayObj):
	def __init__(self, path : str):
		self.__path : str = path
		img = Image.open(path)
		# convert to grayscale
		img = img.convert("L")
		data : List[List[Pixel]] = [[self.__pixval(img.getpixel((x,y))) for y in range(0, img.size[1])] for x in range(img.size[0])]
		super(DisplayObjImage, self).__init__(data)

	@staticmethod
	def __pixval(px):
		return Pixel.LIGHT if px >= 128 else Pixel.DARK