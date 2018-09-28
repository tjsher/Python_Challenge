from __future__ import print_function

class Clean_robot(object):
    """docstring for Clean_robot"""
    def __init__(self, map,position,depth = 0):
        super(Clean_robot, self).__init__

        self.map = map # n * n matrix, * -wall and obtacle '-' - dirty, 'o' -clean
        self.position = position # dictionary{'x': ,'y': }
        self.depth = depth

    def print_map(self):
        for raw in range(len(self.map)):
            for col in range(len(self.map[0])):
                if(raw == self.position['x'] and col == self.position['y']): #enconter robot
                    print('@ ',end ='')#show the position of robot
                else:
                    print(self.map[raw][col],end='')
        print('\n')

    def choose_way(self):# choose order: up left down right  '*' means wall
        stack = [] #store the direction 
        if(self.map[self.position['x'] -1][self.position['y'] ] != '*'):#can move
            stack.append('up')
        if(self.map[self.position['x'] ][self.position['y'] +1] != '*'):#can move
            stack.append('right')
        if(self.map[self.position['x'] +1][self.position['y'] ] != '*'):#can move
            stack.append('down')
        if(self.map[self.position['x'] ][self.position['y'] -1] != '*'):#can move
            stack.append('left')
        return stack

    def move(self):
        if(self.depth >= 100):#control the trace back times
            return
        for direction in self.choose_way():
            if(direction == 'up'):# go up
                self.position['x'] -=1 
                self.print_map()
                self.move() # trace back
            if(direction == 'right'): # go right
                self.position['y'] +=1
                self.print_map()
                self.move()# trace back
            if(direction == 'down'): # go down
                self.position['x'] +=1
                self.print_map()
                self.move()# trace back
            if(direction == 'left'):# go left
                self.position['y'] -=1
                self.print_map()
                self.move()# trace back

    def clean(self):
        self.map[self.position['x']][self.position['y']] = 'o'# cleaned
        self.move()

def main():
    map = [# n * n matrix, * -wall and obtacle '-' - dirty, 'o' -clean
    ['*','*','*','*','*'],
    ['*','-','-','-','*'],
    ['*','-','-','-','*'],
    ['*','-','-','-','*'],
    ['*','*','*','*','*'],
    ]
    pos = {'x' : 2,'y' : 2}
    clean_robot = Clean_robot(map,pos)
    clean_robot.clean()
main()
