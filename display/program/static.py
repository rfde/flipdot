import math

from display.canvas import DisplayCanvas
from display.program.base import DisplayProgram
from display.object.base import DisplayObj

class DisplayProgramStatic(DisplayProgram):
	def __init__(self, obj : DisplayObj, canvas : DisplayCanvas, canvas_x : int = 0, canvas_y : int = 0):
		self.__obj = obj
		# x or y = -1 means center over full width/height.
		if canvas_x == -1:
			canvas_x = math.floor((canvas.num_columns() - obj.num_columns()) / 2)
		if canvas_y == -1:
			canvas_y = math.floor((canvas.num_rows() - obj.num_rows()) / 2)
		update_interval = 10
		super(DisplayProgramStatic, self).__init__(canvas, canvas_x, canvas_y, update_interval)

	def _update_internal(self) -> None:
		self.__obj.draw(self._canvas, self._canvas_x, self._canvas_y, 0, 0)