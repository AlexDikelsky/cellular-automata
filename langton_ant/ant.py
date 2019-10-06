class Ant:
    def __init__(self):
        self.direction = 0
        self.x = 0 
        self.y = 0
        #0 = up
        #1 = right
        #2 = down
        #3 = left

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_direction(self):
        return self.direction

    def right(self):
        #0 -> 1
        #1 -> 2
        #2 -> 3
        #3 -> 0
        self.direction = (self.direction + 1) % 4

    def left(self):
        #0 -> 3
        #1 -> 0
        #2 -> 1
        #3 -> 2
        self.direction = (self.direction + 3) % 4

    def forward(self):
        if self.direction is 0:   #Forward increases y
            self.y += 1
        elif self.direction is 1:
            self.x += 1
        elif self.direction is 2:
            self.y -= 1
        elif self.direction is 3:
            self.x -= 1
        else:
            raise RuntimeError('This should never happen')




