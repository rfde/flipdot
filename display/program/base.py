from abc import ABC, abstractmethod

from display.canvas import DisplayCanvas

class DisplayProgram(ABC):
	def __init__(self, canvas : DisplayCanvas, canvas_x : int = 0, canvas_y : int = 0, update_interval = 1):
		self._canvas = canvas
		self._canvas_x = canvas_x
		self._canvas_y = canvas_y
		self._update_interval = update_interval

	def update(self, timer : int) -> bool:
		if timer % self._update_interval == 0:
			self._update_internal()
			return True
		return False

	@abstractmethod
	def _update_internal(self) -> None:
		pass

