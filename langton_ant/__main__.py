import ant
import grid
import time

size = int(input("How large a grid do you want? : "))

print("Do you want to step through the positions, or just see a specific position?")
step_through = int(input("Type 1 to step, or 0 to jump to a point: "))

if step_through == 0:
    steps = int(input("How many steps? : "))
    i = 0
else:
    print("Press enter repeatedly to continue, or type 'q' to exit")
    steps = -1
    i = 0

traveler = ant.Ant()
plot = grid.Grid(size)

done = False
while not done:
    x = traveler.get_x()
    y = traveler.get_y()
    #print(x, y, traveler.get_direction())

    if plot.get_color(x, y) is 0:
        traveler.right()
    else:
        traveler.left()

    plot.change_color(x, y)

    traveler.forward()
    if step_through == 1:
        if input() == "q":
            done = True
        else:
            print(plot)
    else:
        if i > steps:
            done = True

    i += 1
       
    #print(x, y, traveler.get_direction())
    #time.sleep(0.075)

print(plot)
