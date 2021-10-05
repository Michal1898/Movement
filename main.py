souradnicexy = [(0, 0)]
x = 0


def pohyb(souradnice, smer):
    actual_position=souradnice[0]
    if smer == 's':
        new_position=(actual_position[0],actual_position[1]-1)
    elif smer == 'z':
        new_position=(actual_position[0]-1,actual_position[1])
    elif smer == 'v':
        new_position=(actual_position[0]+1,actual_position[1])
    elif smer == 'j':
        new_position=(actual_position[0],actual_position[1]-1)

    souradnicexy.append(new_position)

pohyb(souradnicexy, 'j')
print(souradnicexy)
pohyb(souradnicexy, 'v')
print(souradnicexy)
pohyb(souradnicexy, 'v')
print(souradnicexy)
pohyb(souradnicexy, 'j')
print(souradnicexy)