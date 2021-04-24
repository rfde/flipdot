from display.content import Pixel, DisplayContent
from display.simulation import DisplaySimulation
from display.flipdot import DisplayFlipdot
from display.object.charsequence import DisplayObjCharSequence
from display.object.image import DisplayObjImage

COLUMNS=28
ROWS=13

content = DisplayContent(columns=COLUMNS, rows=ROWS)
sim = DisplaySimulation(COLUMNS, ROWS, content)

# img = DisplayObjImage("example.gif")
# img.insert(content)
# content.invert()
# sim.refresh()

content.set_all(Pixel.DARK)

seq = DisplayObjCharSequence("Hallo")
seq.insert(content, 0, 3)
sim.refresh()