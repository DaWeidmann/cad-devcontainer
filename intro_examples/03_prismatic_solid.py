from build123d import *
from ocp_vscode import show

length, width, thickness = 80.0, 60.0, 10.0

with BuildPart() as ex3:
    with BuildSketch() as ex3_sk:
        Circle(width)
        Rectangle(length / 2, width / 2,
                     mode=Mode.SUBTRACT)
    extrude(amount=2 * thickness)

show(ex3)
