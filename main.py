souradnicexy = [(0, 0)]


def pohyb(coordinates, direction):
    actual_position = coordinates[len(coordinates) - 1]
    movement_parameters = {"s": (0, -1), "j": (0, +1), "z": (-1, 0), "v": (+1, 0)}
    if direction in movement_parameters:
        new_position = (
            actual_position[0] + movement_parameters[direction][0],
            actual_position[1] + movement_parameters[direction][1],
        )
    coordinates.append(new_position)


print(souradnicexy)
pohyb(souradnicexy, "s")
print(souradnicexy)
pohyb(souradnicexy, "s")
print(souradnicexy)
pohyb(souradnicexy, "z")
print(souradnicexy)
pohyb(souradnicexy, "j")
print(souradnicexy)
pohyb(souradnicexy, "v")
print(souradnicexy)
pohyb(souradnicexy, "j")
print(souradnicexy)
