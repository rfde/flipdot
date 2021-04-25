from abc import ABC, abstractmethod
from typing import Tuple

from display.pixel import Pixel

class DisplayFilter(ABC):
	def __init__(self):
		pass

	def filter_value(self, value : Pixel) -> Pixel:
		return value

	def filter_coordinate(self, column : int, row : int) -> Tuple[int, int]:
		return (column, row)