import grid

a = grid.Grid(5)

tests = [
            [1, 1], [-1, 1], [-1, -1], [1, -1]
        ]

for point in tests:
    print(point)
    a.change_color(point[0], point[1])
    print(a)

#a.change_color(1,  1)
#a.change_color(-1,  1)
#a.change_color(-1, -1)
#a.change_color( 1, -1)

