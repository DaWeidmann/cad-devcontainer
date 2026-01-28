from build123d import *
from ocp_vscode import show

length, width, thickness = 80.0, 60.0, 10.0

with BuildPart() as ex1:
    Box(length, width, thickness)

show(ex1)

