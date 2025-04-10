# Edited by Dan for Git Exercise 1

import math

def calculate_volume_of_sphere(radius):
    return (4/3) * math.pi * radius**3

radii = [30, 40]
for r in radii:
    volume = calculate_volume_of_sphere(r)
    print("Radius:", r, "| Volume:", round(volume, 2))
