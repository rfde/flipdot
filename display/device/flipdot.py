import serial
from typing import Optional

from display.device.base import DisplayDevice
from display.canvas import DisplayCanvas

class DisplayDeviceFlipdot(DisplayDevice):
	def __init__(self, columns : int, rows : int, canvas : DisplayCanvas, ttydev : str):
		super(DisplayDeviceFlipdot, self).__init__(columns, rows, canvas)
		self.__serial : serial.Serial = serial.Serial(
			port=ttydev,
			baudrate=38400,
			timeout=1,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE
		)
		self.__previous_canvas : Optional[DisplayCanvas] = None

	def refresh(self):
		# TODO: compute difference to __previous_canvas and send difference to display
		pass