import time
import math

from display.pixel import Pixel
from display.canvas import DisplayCanvas
from display.device.simulation import DisplayDeviceSimulation
from display.device.flipdot import DisplayDeviceFlipdot
from display.object.charsequence import DisplayObjCharSequence, Font
from display.object.image import DisplayObjImage
from display.filter.invert import DisplayFilterInvert
from display.filter.rotate180 import DisplayFilterRotate180

from display.program.static import DisplayProgramStatic
from display.program.marquee import DisplayProgramMarquee, MarqueeDirection
from display.program.clock import DisplayProgramClock, ClockMode

COLUMNS=28
ROWS=13

canvas = DisplayCanvas(columns=COLUMNS, rows=ROWS)
sim_f = DisplayDeviceSimulation(COLUMNS, ROWS, canvas)
sim_u = DisplayDeviceSimulation(COLUMNS, ROWS, canvas, False)
# flipd = DisplayDeviceFlipdot(COLUMNS, ROWS, canvas, "/dev/ttyUSB0")

canvas.add_filter(DisplayFilterRotate180(canvas.num_columns(), canvas.num_rows()))

programs = [
	# DisplayProgramStatic(
	# 	DisplayObjCharSequence("21:35", Font.NUMERICWIDE6),
	# 	canvas, -1, 0
	# ),
	# DisplayProgramStatic(
	# 	DisplayObjCharSequence("00000", Font.NUMERICWIDE6),
	# 	canvas, -1, 7
	# )
	# DisplayProgramMarquee(
	# 	DisplayObjCharSequence("01.05.2021", Font.NUMERICWIDE6),
	# 	MarqueeDirection.RTL,
	# 	canvas, 0, 7
	# )
	DisplayProgramClock(ClockMode.TIME_HM, canvas, 0),
	DisplayProgramClock(ClockMode.DATE_DM, canvas, 7)
]

timer : int = 0
while True:
	changed : int = 0
	for program in programs:
		if program.update(timer):
			changed += 1

	if changed > 0:
		sim_f.refresh()
		sim_u.refresh()
		# flipd.refresh()

	timer += 1
	time.sleep(1)