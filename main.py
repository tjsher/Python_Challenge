from __future__ import print_function

class Clean_robot(object):
    """docstring for Clean_robot"""
    def __init__(self, map,position):
        super(Clean_robot, self).__init__

        self.map = map # n * n matrix, * -wall and obtacle '-' - dirty, 'o' -clean
        self.position = position # dictionary{'x': ,'y': }

    def print_map(self):
        for raw in range(len(self.map)):
            for col in range(len(self.map[0])):
                if(raw == self.position['x'] and col == self.position['y']):
                    print('@ ',end ='')
                else:
                    print(self.map[raw][col],end='')
        print('\n')

    def choose_way(self):# choose order: up down left right
        stack = []
        if(self.map[self.position['x'] -1][self.position['y'] ] != '*'):#can move
            stack.append('up')
        if(self.map[self.position['x'] ][self.position['y'] +1] != '*'):
            stack.append('right')
        if(self.map[self.position['x'] +1][self.position['y'] ] != '*'):
            stack.append('down')
        if(self.map[self.position['x'] ][self.position['y'] -1] != '*'):
            stack.append('left')
        return stack

    def move(self):
        for direction in self.choose_way():
            if(direction == 'up'):
                self.position['x'] -=1
                self.print_map()
                self.move()
            if(direction == 'right'):
                self.position['y'] +=1
                self.print_map()
                self.move()
            if(direction == 'down'):
                self.position['x'] +=1
                self.print_map()
                self.move()
            if(direction == 'left'):
                self.position['y'] -=1
                self.print_map()
                self.move()

    def clean(self):
        self.move()

def main():
    map = [
    ['*','*','*','*','*'],
    ['*','-','-','-','*'],
    ['*','-','-','-','*'],
    ['*','-','-','-','*'],
    ['*','*','*','*','*'],
    ]
    pos = {'x' : 2,'y' : 2}
    clean_robot = Clean_robot(map,pos)
    clean_robot.print_map()
main()
