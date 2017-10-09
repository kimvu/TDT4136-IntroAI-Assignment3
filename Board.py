from tkinter import *


class Board:
    colors = {
        '.': 'white',       # untried
        '#': 'black',       # obstacle
        'A': 'red',         # start
        'B': 'Lawn Green',  # finish
        'w': 'blue',        # water
        'm': 'grey',        # mountains
        'f': 'darkgreen',   # forest
        'g': 'lightgreen',  # grasslands
        'r': 'sienna'       # roads
    }

    colors_values = {
        '.': 0,  # untried
        '#': 0,  # obstacle
        'A': 0,  # start
        'B': 0,  # finish
        'w': 100,  # water
        'm': 50,  # mountains
        'f': 10,  # forest
        'g': 5,  # grasslands
        'r': 1  # roads
    }

    root = None
    list = []
    start_node = None
    goal_node = None

    def __init__(self, file):
        self.file = file
        self.root = Tk()
        for i, line in enumerate(file):  # create the skeleton of the board and detect goal and start points
            for j, symbol in enumerate(line):
                if symbol == '\n':
                    continue
                c = Canvas(self.root, width=30, height=30, bg=self.colors[symbol])
                c.grid(column=j, row=i)
                node = Node(i, j, None, 0, symbol)
                if symbol == 'B':
                    self.goal_node = node
                if symbol == 'A':
                    self.start_node = node

        self.create_board()

    def create_board(self):  # creates the board with colors and values
        for i, line in enumerate(self.file):
            for j, symbol in enumerate(line):
                if symbol == '\n':
                    continue
                if symbol != '#':
                    c = Canvas(self.root, width=30, height=30, bg=self.colors[symbol])
                    c.grid(column=j, row=i)
                    value = abs(self.goal_node.j - j) + abs(self.goal_node.i - i)
                    c.create_text(15,15,fill="darkblue", font="Times 10 italic bold",
                                  text=value)
                    node = Node(i, j, value, self.colors_values[symbol], symbol)
                    if symbol == 'B':
                        self.goal_node = node
                    if symbol == 'A':
                        self.start_node = node
                    self.list.append(node)

    def update(self):  # updates the board
        self.root.update()

    def addCanvas(self, color, col, row, value):  # method used to change the node
        c = Canvas(self.root, width=30, height=30, bg=color)
        c.grid(column=col, row=row)
        c.create_text(15, 15, fill="darkblue", font="Times 10 italic bold", text=value)

    def getboard(self): # returns the board
        return self.root


class Node: # Node class
    def __init__(self, i, j, value, cost, char):
        self.children = []
        self.parent = None
        self.value = value
        self.g_score = 0
        self.cost = cost
        self.i = i
        self.j = j
        self.visited = False
        self.touched = False
        self.char = char