from build123d import *
from ocp_vscode import show

a, b = 40, 4

with BuildPart() as ex13:
    Cylinder(radius=50, height=10)
    with Locations(ex13.faces().sort_by(Axis.Z)[-1]):
        with PolarLocations(radius=a, count=4):
            CounterSinkHole(radius=b, counter_sink_radius=2 * b)
        with PolarLocations(radius=a, count=4,
                               start_angle=45, angular_range=360):
            CounterBoreHole(radius=b,
                               counter_bore_radius=2 * b,
                               counter_bore_depth=b)

show(ex13)
