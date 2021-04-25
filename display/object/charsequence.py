from typing import Dict, List

from display.content import Pixel, DisplayContent
from display.object.base import DisplayObj

L = Pixel.LIGHT
D = Pixel.DARK

class DisplayObjCharSequence(DisplayObj):
	CHARACTERS : Dict[str, List[List[Pixel]]] = {
		"inter-character-space": [
			[D, D, D, D, D, D, D]
		],
		"A": [
			[L, L, L, L, L, L, L],
			[L, D, D, L, D, D, D],
			[L, L, L, L, L, L, L]
		],
		"B": [
			[L, L, L, L, L, L, L],
			[L, D, D, L, D, D, L],
			[D, L, L, L, L, L, L]
		],
		"C": [
			[L, L, L, L, L, L, L],
			[L, D, D, D, D, D, L]
		],
		"D": [
			[L, L, L, L, L, L, L],
			[L, D, D, D, D, D, L],
			[D, L, L, L, L, L, L]
		],
		"E": [
			[L, L, L, L, L, L, L],
			[L, D, D, L, D, D, L]
		],
		"F": [
			[L, L, L, L, L, L, L],
			[L, D, D, L, D, D, D]
		],
		"G": [
			[L, L, L, L, L, L, L],
			[L, D, D, D, D, D, L],
			[L, D, D, L, L, L, L]
		],
		"H": [
			[L, L, L, L, L, L, L],
			[D, D, D, L, D, D, D],
			[L, L, L, L, L, L, L],
		],
		"I": [
			[L, L, L, L, L, L, L]
		],
		"J": [
			[D, D, D, D, L, L, L],
			[D, D, D, D, D, D, L],
			[L, L, L, L, L, L, L]
		],
		"K": [
			[L, L, L, L, L, L, L],
			[D, D, D, L, D, D, D],
			[L, L, L, D, L, L, L]
		],
		"L": [
			[L, L, L, L, L, L, L],
			[D, D, D, D, D, D, L]
		],
		"M": [
			[L, L, L, L, L, L, L],
			[L, D, D, D, D, D, D],
			[L, L, L, L, L, L, L],
			[L, D, D, D, D, D, D],
			[L, L, L, L, L, L, L],
		],
		"N": [
			[L, L, L, L, L, L, L],
			[L, D, D, D, D, D, D],
			[L, L, L, L, L, L, L]
		],
		"O": [
			[L, L, L, L, L, L, L],
			[L, D, D, D, D, D, L],
			[L, L, L, L, L, L, L]
		],
		"P": [
			[L, L, L, L, L, L, L],
			[L, D, D, L, D, D, D],
			[L, L, L, L, D, D, D]
		],
		"Q": [
			[L, L, L, L, L, L, D],
			[L, D, D, D, D, L, L],
			[L, L, L, L, L, L, D]
		],
		"R": [
			[L, L, L, L, L, L, L],
			[L, D, D, L, L, D, D],
			[L, L, L, L, D, L, L]
		],
		"S": [
			[L, L, L, L, D, D, L],
			# [L, D, D, L, D, D, L],
			[L, D, D, L, L, L, L]
		],
		"T": [
			[L, D, D, D, D, D, D],
			[L, L, L, L, L, L, L],
			[L, D, D, D, D, D, D]
		],
		"U": [
			[L, L, L, L, L, L, L],
			[D, D, D, D, D, D, L],
			[L, L, L, L, L, L, L]
		],
		"V": [
			[L, L, L, L, L, L, D],
			[D, D, D, D, D, D, L],
			[L, L, L, L, L, L, D]
		],
		"W": [
			[L, L, L, L, L, L, L],
			[D, D, D, D, D, D, L],
			[L, L, L, L, L, L, L],
			[D, D, D, D, D, D, L],
			[L, L, L, L, L, L, L]
		],
		"X": [
			[L, L, L, D, L, L, L],
			[D, D, D, L, D, D, D],
			[L, L, L, D, L, L, L]
		],
		"Y": [
			[L, L, L, L, D, D, D],
			[D, D, D, L, L, L, L],
			[L, L, L, L, D, D, D]
		],
		"Z": [
			[L, D, D, D, L, L, L],
			[L, D, D, L, D, D, L],
			[L, L, L, D, D, D, L]
		],
		"Ä": [
			[L, D, L, L, L, L, L],
			[D, D, L, D, L, D, D],
			[L, D, L, L, L, L, L]
		],
		"Ö": [
			[L, D, L, L, L, L, L],
			[D, D, L, D, D, D, L],
			[L, D, L, L, L, L, L]
		],
		"Ü": [
			[L, D, L, L, L, L, L],
			[D, D, D, D, D, D, L],
			[L, D, L, L, L, L, L]
		],
		"0": [
			[L, L, L, L, L, L, L],
			[L, D, D, D, D, D, L],
			[L, L, L, L, L, L, L]
		],
		"1": [
			[L, L, L, L, L, L, L],
		],
		"2": [
			[L, D, D, L, L, L, L],
			# [L, D, D, L, D, D, L],
			[L, L, L, L, D, D, L]
		],
		"3": [
			[L, D, D, L, D, D, L],
			[L, L, L, L, L, L, L]
		],
		"4": [
			[L, L, L, L, D, D, D],
			[D, D, D, L, D, D, D],
			[L, L, L, L, L, L, L]
		],
		"5": [
			[L, L, L, L, D, D, L],
			# [L, D, D, L, D, D, L],
			[L, D, D, L, L, L, L]
		],
		"6": [
			[L, L, L, L, L, L, L],
			[L, D, D, L, D, D, L],
			[L, D, D, L, L, L, L]
		],
		"7": [
			[L, D, D, D, D, D, D],
			[L, L, L, L, L, L, L]
		],
		"8": [
			[L, L, L, L, L, L, L],
			[L, D, D, L, D, D, L],
			[L, L, L, L, L, L, L]
		],
		"9": [
			[L, L, L, L, D, D, L],
			[L, D, D, L, D, D, L],
			[L, L, L, L, L, L, L]
		],
		".": [
			[D, D, D, D, D, D, L]
		],
		":": [
			[D, D, L, D, L, D, D]
		],
		"!": [
			[L, L, L, L, L, D, L]
		],
		"-": [
			[D, D, D, L, D, D, D],
			[D, D, D, L, D, D, D]
		],
		"+": [
			[D, D, D, L, D, D, D],
			[D, D, L, L, L, D, D],
			[D, D, D, L, D, D, D]
		],
		"*": [
			[D, L, D, D, D, D, D],
			[L, L, L, D, D, D, D],
			[D, L, D, D, D, D, D]
		],
		"/": [
			[D, D, D, D, L, L, L],
			[L, L, L, L, D, D, D]
		],
		"\\": [
			[L, L, L, L, D, D, D],
			[D, D, D, D, L, L, L]
		],
		"=": [
			[D, D, L, D, L, D, D],
			[D, D, L, D, L, D, D]
		],
		"_": [
			[D, D, D, D, D, D, L],
			[D, D, D, D, D, D, L],
			[D, D, D, D, D, D, L]
		],
		" ": [
			[D, D, D, D, D, D, D],
		],
		"(": [
			[D, L, L, L, L, L, D],
			[L, D, D, D, D, D, L]
		],
		")": [
			[L, D, D, D, D, D, L],
			[D, L, L, L, L, L, D]
		],
		"[": [
			[L, L, L, L, L, L, L],
			[L, D, D, D, D, D, L]
		],
		"]": [
			[L, D, D, D, D, D, L],
			[L, L, L, L, L, L, L]
		],
		"'": [
			[L, L, D, D, D, D, D]
		],
		"\"": [
			[L, L, D, D, D, D, D],
			[D, D, D, D, D, D, D],
			[L, L, D, D, D, D, D]
		],
		"?": [
			[L, D, D, D, D, D, D],
			[L, D, D, L, L, D, L],
			[L, L, L, L, D, D, D]
		],
		"@": [
			[L, L, L, L, L, L, L],
			[L, D, D, D, D, D, L],
			[L, D, L, L, L, D, L],
			[L, D, L, D, L, D, L],
			[L, L, L, L, L, D, L],
		],
		">": [
			[D, L, D, D, D, L, D],
			[D, D, L, D, L, D, D],
			[D, D, D, L, D, D, D]
		],
		"<": [
			[D, D, D, L, D, D, D],
			[D, D, L, D, L, D, D],
			[D, L, D, D, D, L, D]
		],
		"#": [
			[D, D, L, D, L, D, D],
			[D, L, L, L, L, L, D],
			[D, D, L, D, L, D, D],
			[D, L, L, L, L, L, D],
			[D, D, L, D, L, D, D]
		],
	}

	def __init__(self, string : str):
		data : List[List[Pixel]] = []
		self.__string : str = string
		string : str = string.upper()
		for char in string:
			if not char in DisplayObjCharSequence.CHARACTERS:
				print(f"WARN: Unknown character '{char}'")
				continue
			data.extend(DisplayObjCharSequence.CHARACTERS[char])
			data.extend(DisplayObjCharSequence.CHARACTERS["inter-character-space"])
		data.pop() # remove last inter-character-space
		super(DisplayObjCharSequence, self).__init__(data)