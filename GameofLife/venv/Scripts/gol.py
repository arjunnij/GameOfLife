import pygame as pg

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
CELL_WIDTH = 10
CELL_HEIGHT = 10
BORDER_THICKNESS = 1
BOARD_WIDTH = 50
BOARD_HEIGHT = 50
BACKGROUND_COLOR = "blue"
CELL_COLOR = "grey"
ALIVE_COLOR = "yellow"
START_BUTTON_COLOR = "green"
START_BUTTON_WIDTH = 100
START_BUTTON_HEIGHT = 50
START_BUTTON_Y = 100
STOP_BUTTON_COLOR = "red"

class Cell(pg.Rect):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = CELL_WIDTH
        self.height = CELL_HEIGHT
        self.alive = False
        self.alive_next = False

class game_of_life:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.started_simulation = False
        self.exited = False
        self.board = []
        self.BOARD_WIDTH_IN_PIXELS = (BOARD_WIDTH * (CELL_WIDTH + BORDER_THICKNESS))
        self.BOARD_HEIGHT_IN_PIXELS = (BOARD_HEIGHT * (CELL_HEIGHT + BORDER_THICKNESS))
        self.BOARD_TOP_X = self.screen.get_width() / 2 -  self.BOARD_WIDTH_IN_PIXELS / 2
        self.BOARD_TOP_Y = self.screen.get_height() / 2 - self.BOARD_HEIGHT_IN_PIXELS / 2
        self.START_BUTTON_X = (self.BOARD_TOP_X + (self.BOARD_WIDTH_IN_PIXELS / 2) - START_BUTTON_WIDTH / 2)
        self.START_BUTTON_Y = self.BOARD_TOP_Y + self.BOARD_HEIGHT_IN_PIXELS + 20
        self.drag = False

    def initialize_board(self):
        self.screen.fill(pg.Color(BACKGROUND_COLOR))
        self.start_button = pg.draw.rect(self.screen, pg.Color(START_BUTTON_COLOR), pg.Rect(self.START_BUTTON_X, self.START_BUTTON_Y, START_BUTTON_WIDTH, START_BUTTON_HEIGHT))
        y = self.BOARD_TOP_Y

        for i in range(0, BOARD_HEIGHT):
            self.board.append([])
            x = self.BOARD_TOP_X

            for j in range(0, BOARD_WIDTH):
                self.board[i].append(Cell(x, y))
                pg.draw.rect(self.screen, pg.Color(CELL_COLOR), self.board[i][j])
                x += (CELL_WIDTH + BORDER_THICKNESS)

            y += (CELL_HEIGHT + BORDER_THICKNESS)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.exited = True
            if event.type == pg.MOUSEBUTTONDOWN or self.drag == True:
                self.drag = True
                mouse_position = pg.mouse.get_pos()

                if (self.start_button.collidepoint(mouse_position) and self.screen.get_at(
                        (mouse_position[0], mouse_position[1])) == pg.Color(START_BUTTON_COLOR)):
                    pg.draw.rect(self.screen, pg.Color(STOP_BUTTON_COLOR), self.start_button)
                    self.started_simulation = True

                for row in self.board:
                    for cell in row:
                        if (cell.collidepoint(mouse_position)):
                            cell.alive = True
                            cell.alive_next = True

            if event.type == pg.MOUSEBUTTONUP:
                self.drag = False

    def return_alive(self, row, col):
        num_neighbors_alive = 0
        num_neighbors_dead = 0

        if (row > 0):
            if (self.board[row - 1][col].alive):
                num_neighbors_alive += 1

            elif (not self.board[row - 1][col].alive):
                num_neighbors_dead += 1

            if(col > 0):
                if(self.board[row - 1][col - 1].alive):
                    num_neighbors_alive += 1
                else:
                    num_neighbors_dead += 1

            if(col < BOARD_WIDTH - 1):
                if(self.board[row - 1][col + 1].alive):
                    num_neighbors_alive += 1
                else:
                    num_neighbors_dead += 1
        if (col > 0):
            if (self.board[row][col - 1].alive):
                num_neighbors_alive += 1

            elif (not self.board[row][col - 1].alive):
                num_neighbors_dead += 1

            if(row < BOARD_HEIGHT - 1):
                if(self.board[row + 1][col - 1].alive):
                    num_neighbors_alive += 1
                else:
                    num_neighbors_dead += 1

        if (col < BOARD_WIDTH - 1):
            if (self.board[row][col + 1].alive):
                num_neighbors_alive += 1

            elif (not self.board[row][col + 1].alive):
                num_neighbors_dead += 1

            if(row < BOARD_HEIGHT - 1):
                if(self.board[row + 1][col + 1].alive):
                    num_neighbors_alive += 1
                else:
                    num_neighbors_dead += 1

        if (row < BOARD_HEIGHT - 1):
            if (self.board[row + 1][col].alive):
                num_neighbors_alive += 1
            elif (not self.board[row + 1][col].alive):
                num_neighbors_dead += 1

        return (num_neighbors_alive, num_neighbors_dead)

    def conways_rules(self):
        for row in range (0, BOARD_WIDTH):
            for col in range (0, BOARD_HEIGHT):
                alive_and_dead = self.return_alive(row, col)
                num_neighbors_alive = alive_and_dead[0]
                num_neighbors_dead = alive_and_dead[1]

                if(self.board[row][col].alive):
                    if(num_neighbors_alive == 2 or num_neighbors_alive == 3):
                        self.board[row][col].alive_next = True
                    elif(num_neighbors_alive > 3):
                        self.board[row][col].alive_next = False
                    elif (num_neighbors_dead >= 2):
                        # print("were more than 2 dead")
                        self.board[row][col].alive_next = False
                else:
                    if(num_neighbors_alive == 3):
                        self.board[row][col].alive_next = True
    def run(self):
        # initialize the board
        self.initialize_board()
        pg.display.flip()

        while not self.started_simulation and not self.exited:
                self.handle_events()
                self.update_board()
                pg.display.flip()

        clock = pg.time.Clock()

        while self.started_simulation and not self.exited:
            self.handle_events()
            self.conways_rules()
            self.update_board()
            pg.time.wait(1000)
            pg.display.flip()

    def update_board(self):
        for row in self.board:
            for cell in row:
                if(cell.alive_next == True):
                    #print("cell should be alive next")
                    pg.draw.rect(self.screen, pg.Color(ALIVE_COLOR), cell)
                    cell.alive = True
                else:
                    pg.draw.rect(self.screen, pg.Color(CELL_COLOR), cell)
                    cell.alive = False



if __name__ == "__main__":
    game = game_of_life()
    game.run()

