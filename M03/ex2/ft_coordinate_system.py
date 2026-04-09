#!/usr/bin/env python3

import math
import sys

def parse_coords(prompt):
    while True:
        raw = input(prompt)
        parts = raw.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        coords = []
        error = False
        for part in parts:
            try:
                coords.append(float(part.strip()))
            except ValueError as e:
                print(f"Error on parameter '{part.strip()}': {e}")
                error = True
                break
        if not error:
            return tuple(coords)


def distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)


print("=== Game Coordinate System ===")

print("Get a first set of coordinates")
p1 = parse_coords("Enter new coordinates as floats in format 'x,y,z': ")
print(f"Got a first tuple: {p1}")
print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")
print(f"Distance to center: {distance((0.0, 0.0, 0.0), p1):.4f}")

print("Get a second set of coordinates")
p2 = parse_coords("Enter new coordinates as floats in format 'x,y,z': ")
print(f"Distance between the 2 sets of coordinates: {distance(p1, p2):.4f}")