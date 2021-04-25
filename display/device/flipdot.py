import serial
import time
from typing import Optional, List, Tuple

from display.device.base import DisplayDevice
from display.canvas import DisplayCanvas
from display.pixel import Pixel

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

	def __del__(self):
		self.__serial.close()

	def __send_msg(self, send_msg : str, expect_msg : str) -> bool:
		self.__serial.write(send_msg)
		return self.__serial.read(len(expect_msg)) == expect_msg

	@staticmethod
	def __column_vector_to_dec(vector : List[Pixel]) -> Tuple[int,int]:
		result : int = 0
		for i in range(len(vector)):
			if vector[i] == Pixel.LIGHT:
				result = result | (1 << i)
		return (result & 0xff, result >> 8)

	def refresh(self):
		columns_to_refresh : List[Tuple[int, List[Pixel]]] = self._canvas.diff_column_vectors(self.__previous_canvas)
		for column in columns_to_refresh:
			column_id : int = column[0] + 1
			column_dec_lo, column_dec_hi = DisplayDeviceFlipdot.__column_vector_to_dec(column[1])
			self.__send_msg(
				send_msg=bytes(f"{column_id};{column_dec_lo};{column_dec_hi}\r", encoding="ascii"),
				expect_msg=b"Daten\r"
			)
		self.__send_msg(
			send_msg=b"30\r",
			expect_msg=b"Refresh\r"
		)
		self.__previous_canvas = self._canvas.copy()