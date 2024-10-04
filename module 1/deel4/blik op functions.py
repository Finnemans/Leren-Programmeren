import math
from test_lib import test, report

def inhoud(diameter: float, height: float) -> float:
    radius = diameter / 2
    inhoud = radius * radius * math.pi * height
    return round(inhoud, 1)

diameter = 8.0
height = 5.0
expect_content = 251.3
calculated_content = inhoud(diameter,height)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculated_content )

report()
