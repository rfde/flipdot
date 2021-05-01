import math
from enum import Enum

from display.pixel import Pixel
from display.canvas import DisplayCanvas
from display.program.base import DisplayProgram
from display.object.base import DisplayObj

class MarqueeDirection(Enum):
	RTL = 0
	LTR = 1

class DisplayProgramMarquee(DisplayProgram):
	def __init__(self, obj : DisplayObj, direction : MarqueeDirection, canvas : DisplayCanvas, canvas_x : int = 0, canvas_y : int = 0, update_interval : int = 1):
		self.__obj = obj
		self.__direction = direction
		# y = -1 means center over full width/height.
		if canvas_y == -1:
			canvas_y = math.floor((canvas.num_rows() - obj.num_rows()) / 2)
		super(DisplayProgramMarquee, self).__init__(canvas, canvas_x, canvas_y, update_interval)
		self.__reset_x()

	def __leftmost_offset(self) -> int:
		return -1 * self.__obj.num_columns()

	def __rightmost_offset(self) -> int:
		return self._canvas.num_columns()

	def __reset_x(self) -> None:
		if self.__direction == MarqueeDirection.RTL:
			self.__x = self.__rightmost_offset()
		else:
			self.__x = self.__leftmost_offset()

	def _update_internal(self) -> None:
		self._canvas.set_square(self._canvas_x, self._canvas_y, self._canvas.num_columns(), self.__obj.num_rows(), Pixel.DARK)
		if self.__direction == MarqueeDirection.RTL:
			if self.__x == self.__leftmost_offset():
				self.__reset_x()
			self.__obj.draw(self._canvas, self._canvas_x + self.__x, self._canvas_y, 0, 0)
			self.__x -= 1
		else:
			if self.__x == self.__rightmost_offset():
				self.__reset_x()
			self.__obj.draw(self._canvas, self._canvas_x + self.__x, self._canvas_y, 0, 0)
			self.__x += 1