from tkinter import *
import random


class App:
    def __init__(self):
        # Call start functions
        self.create_interface()
        self.create_apple()
        self.draw_board()
        self.window.bind("<Key>", lambda event: self.key(event))
        self.window.mainloop()

    def create_interface(self):
        self.window = Tk()
        self.window.title("Snake game")
        # Create board
        self.board = []
        for row in range(5):
            for column in range(5):
                cell = {}
                cell["row"] = row
                cell["column"] = column
                self.board.append(cell)
        # Create snake
        self.snake = []
        node = {}
        node["row"] = random.randint(2, 3)
        node["column"] = random.randint(2, 3)
        node["row"] = 2
        node["column"] = 2
        self.snake.append(node)
        self.direction = random.choice([8, 6, 5, 4])
        # Game status
        self.game_over = False

    def create_apple(self):
        while True:
            self.apple = {"row": random.randint(
                0, 4), "column": random.randint(0, 4)}
            if self.apple not in self.snake:
                break

    def move_snake(self):
        # Create new node based on direction
        new_node = self.snake[0].copy()
        if self.direction == 8:
            new_node["row"] -= 1
        elif self.direction == 6:
            new_node["column"] += 1
        elif self.direction == 5:
            new_node["row"] += 1
        elif self.direction == 4:
            new_node["column"] -= 1

        if new_node in self.board and new_node not in self.snake:
            # Insert new node
            self.snake.insert(0, new_node)
            # Remove last node or create a new apple
            if new_node == self.apple:
                self.create_apple()
            else:
                del self.snake[-1]
        else:
            Label(self.window, text="Game Over").grid(
                row=6, column=1, columnspan=5)
            self.game_over = True

        score = "Total score: " + str(len(self.snake))
        Label(self.window, text=score).grid(row=5, column=1, columnspan=5)

    def key(self, event):
        self.direction = int(repr(event.char)[1])

    def draw_board(self):
        if not self.game_over:
            self.move_snake()
            for cell in self.board:
                Label(self.window, text="-",
                      width=3).grid(row=cell["row"], column=cell["column"])
            Label(self.window, text="a", width=3).grid(
                row=self.apple["row"], column=self.apple["column"])
            for node in self.snake:
                Label(self.window, text="O", width=3).grid(
                    row=node["row"], column=node["column"])
            self.window.after(1000, self.draw_board)


app = App()
