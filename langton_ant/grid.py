class Grid:
    def __init__(self, usize):
        self.size = usize
        self.space = [[0 for j in range(usize)] for i in range(usize)]
    def __str__(self):
        s = ""
        for i in self.space:
            for j in i:
                if j == 0:
                    s += " "
                else:
                    s += "#"

                s += " "
            s += "\n"
        return s

    def change_color(self, x, y):
        mid = len(self.space) // 2 

        #It makes more sense for it to be
            #[mid + y]
        #But that gives a horizontal reflection of what most implemations give

        self.space[mid - x][mid - y] = (self.space[mid - x][mid - y] + 1) % 2

    def get_color(self, x, y):
        mid = len(self.space) // 2 
        return self.space[mid - x][mid - y]

#b = Board(5)
#
#for i in range(-2, 3, 2):
#    b.change_color(0, i)
#print(b)
#for i in range(-2, 3, 2):
#    b.change_color(0, i)
#
#print(b)
