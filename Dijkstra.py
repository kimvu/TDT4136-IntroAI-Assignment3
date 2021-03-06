from Board import Board
import time
finished = False
a = 1  # value to keep the correct path to show once


class AlgorithmD:
    current_node = None
    goal_node = None
    start_node = None
    best_child_node = None

    def __init__(self, board):  # initialisation to get current node
        self.board = board
        self.current_node = self.board.start_node
        self.start_node = self.board.start_node
        self.goal_node = self.board.goal_node

    def find_next(self):
        for x in self.board.list:  # detect current node and its children
            if x.i == self.current_node.i + 1 and x.j == self.current_node.j \
                    or x.i == self.current_node.i - 1 and x.j == self.current_node.j \
                    or x.i == self.current_node.i and x.j == self.current_node.j + 1 \
                    or x.i == self.current_node.i and x.j == self.current_node.j - 1:
                if self.best_child_node is None or self.best_child_node.g_score < x.g_score:  # Djikstra only care about g_score
                    self.best_child_node = x
                x.touched = True
                if x.visited is False:  # if the node isn't visited yet the parent of the child (X) becomes current_node
                    x.parent = self.current_node
                x.g_score = x.cost + self.current_node.g_score  # updating the amount it cost to move to x
                self.current_node.children.append(x)
                if x.value == 0:  # if we have node that has value 0 then we have finished
                    global finished
                    finished = True
                if x.visited is False and x != self.goal_node and x != self.start_node:  # All the nodes that are
                                                    # touched and not visited yet is yellow expect the goal and start
                    self.board.addCanvas('yellow', x.j, x.i, x.value)
        if self.start_node != self.current_node and self.goal_node != self.current_node:  # The visited node gets blue
            self.board.addCanvas('Royal Blue', self.current_node.j, self.current_node.i, self.current_node.value)
        self.current_node.visited = True
        if self.best_child_node:
            self.current_node = self.best_child_node
        touched_node = None
        for x in self.board.list:  # loop to find the next best_child_node if there is no more child to the parent
            if x.touched is True and x.visited is False:
                if touched_node is None:
                    touched_node = x
                    continue
                if touched_node.g_score > x.g_score:  # Djikstra only care about g_score
                    touched_node = x
        if touched_node:
            self.best_child_node = touched_node
        self.current_node = self.best_child_node

    def show_correct_path(self):  # simply show the best path in orange color
        correct_parent = self.board.goal_node.parent
        for x in self.board.list:
            self.board.addCanvas(Board.colors[x.char], x.j, x.i, x.value)
        while correct_parent.parent is not None:
            self.board.addCanvas('orange', correct_parent.j, correct_parent.i, correct_parent.value)
            correct_parent = correct_parent.parent


if __name__ == "__main__":
    board1 = Board(open("Boards/board-2-3.txt").readlines())  # This is where i choose my board
    alg = AlgorithmD(board1)
    count = 0  # counts how many steps
    while True:
        if finished is False:
            count = count + 1
            print(count)
            alg.find_next()
        else:
            if a == 1:
                a = 2
                alg.show_correct_path()
        board1.getboard().update()
        time.sleep(0.01)  # Solve speed


