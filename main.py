from display.content import Pixel, DisplayContent
from display.simulation import DisplaySimulation
from display.flipdot import DisplayFlipdot
from display.object.charsequence import DisplayObjCharSequence
from display.object.image import DisplayObjImage

from display.filter.invert import DisplayFilterInvert
from display.filter.rotate180 import DisplayFilterRotate180

COLUMNS=28
ROWS=13

content = DisplayContent(columns=COLUMNS, rows=ROWS)
sim_f = DisplaySimulation(COLUMNS, ROWS, content)
sim_u = DisplaySimulation(COLUMNS, ROWS, content, False)

img = DisplayObjImage("example.gif")
img.insert(content)
sim_f.refresh()
sim_u.refresh()

content.add_filter(DisplayFilterInvert())
content.add_filter(DisplayFilterRotate180(content.num_columns(), content.num_rows()))
sim_f.refresh()
sim_u.refresh()

content.set_all(Pixel.DARK)
seq = DisplayObjCharSequence("Hallo")
seq.insert(content, 0, 3)
sim_f.refresh()
sim_u.refresh()
