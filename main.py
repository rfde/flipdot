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

COLUMNS=28
ROWS=13

canvas = DisplayCanvas(columns=COLUMNS, rows=ROWS)
sim_f = DisplayDeviceSimulation(COLUMNS, ROWS, canvas)
sim_u = DisplayDeviceSimulation(COLUMNS, ROWS, canvas, False)
# flipd = DisplayDeviceFlipdot(COLUMNS, ROWS, canvas, "/dev/ttyUSB0")

canvas.add_filter(DisplayFilterRotate180(canvas.num_columns(), canvas.num_rows()))

# img = DisplayObjImage("example.gif")
# img.draw(canvas)
# sim_f.refresh()
# sim_u.refresh()
# flipd.refresh()

# time.sleep(5)

# canvas.add_filter(DisplayFilterInvert())
# canvas.add_filter(DisplayFilterRotate180(canvas.num_columns(), canvas.num_rows()))
# sim_f.refresh()
# sim_u.refresh()
# flipd.refresh()

# time.sleep(5)

# canvas.set_all(Pixel.DARK)
seq = DisplayObjCharSequence("21:35", Font.NUMERICWIDE6)
seq.draw(canvas, math.floor((canvas.num_columns() - seq.num_columns()) / 2), 0)
seq = DisplayObjCharSequence("01.05.", Font.NUMERICWIDE6)
seq.draw(canvas, math.floor((canvas.num_columns() - seq.num_columns()) / 2), 7)
sim_f.refresh()
sim_u.refresh()
# flipd.refresh()
