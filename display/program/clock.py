import math
from enum import Enum
from datetime import datetime
from typing import Optional

from display.pixel import Pixel
from display.canvas import DisplayCanvas
from display.program.base import DisplayProgram
from display.object.charsequence import DisplayObjCharSequence, Font

class ClockMode(Enum):
	TIME_HM = 0
	TIME_HMS = 0
	DATE_DMY = 1
	DATE_DM = 2
	DOW = 3

class DisplayProgramClock(DisplayProgram):
	def __init__(self, mode : ClockMode, canvas : DisplayCanvas, canvas_y : int = 0):
		self.__mode = mode
		update_interval = 1
		if mode == ClockMode.TIME_HMS:
			update_interval = 5
		super(DisplayProgramClock, self).__init__(canvas, 0, canvas_y, update_interval)

	def _update_internal(self) -> None:
		obj : Optional[DisplayObjCharSequence] = None

		if self.__mode == ClockMode.TIME_HM:
			obj = DisplayObjCharSequence(datetime.now().strftime("%H:%M"), Font.NUMERICWIDE6)
		if self.__mode == ClockMode.TIME_HMS:
			obj = DisplayObjCharSequence(datetime.now().strftime("%H:%M:%S"), Font.CONDENSED6)
		elif self.__mode == ClockMode.DATE_DMY:
			obj = DisplayObjCharSequence(datetime.now().strftime("%d.%m.%y"), Font.CONDENSED6)
		elif self.__mode == ClockMode.DATE_DM:
			obj = DisplayObjCharSequence(datetime.now().strftime("%d.%m."), Font.NUMERICWIDE6)
		elif self.__mode == ClockMode.DOW:
			obj = DisplayObjCharSequence(datetime.now().strftime("%A"), Font.CONDENSED6)

		assert(obj is not None)
		self._canvas.set_square(0, self._canvas_y, self._canvas.num_columns(), obj.num_rows(), Pixel.DARK)
		obj.draw(self._canvas, math.floor((self._canvas.num_columns() - obj.num_columns()) / 2), self._canvas_y, 0, 0)