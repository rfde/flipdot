from typing import List
from display.content import Pixel, DisplayContent
from display.simulation import DisplaySimulation
from display.flipdot import DisplayFlipdot

content = DisplayContent(columns=28, rows=13)
sim = DisplaySimulation(28, 13, content)

sim.refresh()

content.set(0,0, Pixel.LIGHT)
content.set(1,1, Pixel.LIGHT)

sim.refresh()

content.set_all(Pixel.LIGHT)

sim.refresh()

content.set_all(Pixel.DARK)

sim.refresh()