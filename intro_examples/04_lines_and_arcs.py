from build123d import *
from ocp_vscode import show

length, width, thickness = 80.0, 60.0, 10.0

with BuildPart() as ex4:
    with BuildSketch() as ext4_sk:
        with BuildLine() as ex4_ln:
            l1 = Line((0, 0), (length, 0))
            l2 = Line((length, 0), (length, width))
            l3 = ThreePointArc((length, width), (width, width*1.5), (0, width))
            # For tangent arc use the following:
            # l3 = ThreePointArc((length, width),
            #                    (length/2, width+length/2),
            #                    (0, width))
            l4 = Line((0, width), (0, 0))
        make_face()
    extrude(amount=thickness)

show(ex4)
