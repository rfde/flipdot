from display.base import Display
from display.content import DisplayContent

class DisplayFlipdot(Display):
	def __init__(self, columns : int, rows : int, content : DisplayContent):
		super(DisplayFlipdot, self).__init__(columns, rows, content)
		self.__previous_content = content.copy()
		# TODO: set up serial connection and send first content

	def refresh(self):
		# TODO: compute difference to __previous_content and send difference to display
		pass