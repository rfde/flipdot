from display.pixel import Pixel
from display.canvas import DisplayCanvas
from display.device.simulation import DisplayDeviceSimulation
from display.device.flipdot import DisplayDeviceFlipdot
from display.object.charsequence import DisplayObjCharSequence
from display.object.image import DisplayObjImage

from display.filter.invert import DisplayFilterInvert
from display.filter.rotate180 import DisplayFilterRotate180

COLUMNS=28
ROWS=13

canvas = DisplayCanvas(columns=COLUMNS, rows=ROWS)
sim_f = DisplayDeviceSimulation(COLUMNS, ROWS, canvas)
sim_u = DisplayDeviceSimulation(COLUMNS, ROWS, canvas, False)
flipd = DisplayDeviceFlipdot(COLUMNS, ROWS, canvas, "/dev/ttyUSB0")

img = DisplayObjImage("example.gif")
img.insert(canvas)
sim_f.refresh()
sim_u.refresh()
flipd.refresh()

# time.sleep(5)

# canvas.add_filter(DisplayFilterInvert())
# canvas.add_filter(DisplayFilterRotate180(canvas.num_columns(), canvas.num_rows()))
# sim_f.refresh()
# sim_u.refresh()
# flipd.refresh()

# time.sleep(5)

# canvas.set_all(Pixel.DARK)
# seq = DisplayObjCharSequence("Hallo")
# seq.insert(canvas, 0, 3)
# sim_f.refresh()
# sim_u.refresh()
# flipd.refresh()