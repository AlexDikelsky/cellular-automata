import ant
import grid

size = 9
steps = 20

traveler = ant.Ant()
plot = grid.Grid(size)

for i in range(steps):

    x = traveler.get_x()
    y = traveler.get_y()
    print(x, y, traveler.get_direction())

    if plot.get_color(x, y) is 0:
        traveler.right()
    else:
        traveler.left()

    plot.change_color(x, y)

    traveler.forward()
    print(x, y, traveler.get_direction())
    input()
    print(plot)


