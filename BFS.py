from Board import Board
import time
finished = False
a = 1  # value to keep the correct path to show once


class Algorithm:
    current_node = None
    goal_node = None
    start_node = None
    best_child_node = None
    best_child_node_list = []

    def __init__(self, board):  # initialisation to get current node
        self.board = board
        self.best_child_node_list.append(self.board.start_node)
        self.current_node = self.board.start_node
        self.start_node = self.board.start_node
        self.goal_node = self.board.goal_node

    def find_next(self):
        global finished
        if finished is False:
            for y in self.best_child_node_list:
                if y.value == 0:
                    finished = True
                    break
                self.current_node = y
                for x in self.board.list:  # detect current node and its children
                    if x.i == self.current_node.i + 1 and x.j == self.current_node.j \
                            or x.i == self.current_node.i - 1 and x.j == self.current_node.j \
                            or x.i == self.current_node.i and x.j == self.current_node.j + 1 \
                            or x.i == self.current_node.i and x.j == self.current_node.j - 1:
                        if x.parent is None:
                            self.best_child_node_list.append(x)
                        self.best_child_node = x
                        x.touched = True
                        if x.visited is False:  # if the node isn't visited yet the parent of the child (X) becomes current_node
                            x.parent = self.current_node
                        self.current_node.children.append(x)
                        if y.value == 0:  # if we have node that has value 0 then we have finished
                            finished = True
                        if x.visited is False and x != self.goal_node and x != self.start_node:  # All the nodes that are
                            # touched and not visited yet is yellow expect the goal and start
                            self.board.addCanvas('yellow', x.j, x.i, x.value)
                if self.start_node != self.current_node and self.goal_node != self.current_node:  # The visited node gets blue
                    self.board.addCanvas('Royal Blue', self.current_node.j, self.current_node.i,
                                         self.current_node.value)
                self.current_node.visited = True
                if self.best_child_node:
                    self.current_node = self.best_child_node
                self.board.update()



    def show_correct_path(self):  # simply show the best path in orange color
        correct_parent = self.board.goal_node.parent
        for x in self.board.list:
            self.board.addCanvas(Board.colors[x.char], x.j, x.i, x.value)
        while correct_parent.parent is not None:
            self.board.addCanvas('orange', correct_parent.j, correct_parent.i, correct_parent.value)
            correct_parent = correct_parent.parent


if __name__ == "__main__":
    board = Board(open("Boards/board-2-3.txt").readlines())  # This is where i choose my board
    alg = Algorithm(board)
    while True:
        if finished is False:
            print("RUN")
            alg.find_next()
        else:
            if a == 1:
                a = 2
                alg.show_correct_path()
        board.getboard().update()
        time.sleep(0.1)  # Solve speed


