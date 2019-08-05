import unittest
import gol

class TestGameofLife(unittest.TestCase):
    def setUp(self):
        self.game = gol.game_of_life()
        self.game.set_debug_mode(True)
        self.game.run() # this will intialize the board

    # ensure that a cell dies when it has less than two neighbors

    def test_update_logic(self):

        # check to ensure a single cell dies due to starvation

        cell1 = self.game.board[20][20]
        cell1.alive = True;
        self.game.conways_rules() # execute Conway's rules on the board
        self.assertFalse(cell1.alive_next)

        # check to ensure that no cell dies

        cell1 = self.game.board[20][20]
        cell2 = self.game.board[21][20]
        cell3 = self.game.board[20][21]
        cell4 = self.game.board[21][21]
        cell1.alive = True
        cell2.alive = True
        cell3.alive = True
        cell4.alive = True

        self.game.conways_rules()

        # all cells should be alive since they all have exactly three neighbors

        self.assertTrue(cell1.alive_next)
        self.assertTrue(cell2.alive_next)
        self.assertTrue(cell3.alive_next)
        self.assertTrue(cell4.alive_next)

        # this is called a blinker - a special type of oscillator. It will alternate from a horizontal position to a vertical one.

        cell1 = self.game.board[30][30]
        cell2 = self.game.board[30][31]
        cell3 = self.game.board[30][29]

        cell1.alive = True
        cell2.alive = True
        cell3.alive = True

        self.game.conways_rules()

        # ensure the blinker vertically oriented

        self.assertTrue(cell1.alive_next)
        self.assertFalse(cell2.alive_next)
        self.assertFalse(cell3.alive_next)
        self.assertTrue(self.game.board[29][30].alive_next)
        self.assertTrue(self.game.board[31][30].alive_next)

    def test_total_overcrowding(self):
        self.game.set_debug_mode(True)
        self.game.run()
        
        for row in range(0, gol.BOARD_HEIGHT):
            for col in range (0, gol.BOARD_WIDTH):
                self.game.board[row][col].alive = True
                self.game.board[row]

        self.game.conways_rules()

        for row in range(0, len(self.game.board)):
            for col in range(0, len(self.game.board[row])):
                if(row == 0 and col == 0):
                    self.assertTrue(self.game.board[row][col].alive_next)
                elif(row == gol.BOARD_HEIGHT - 1 and col == gol.BOARD_WIDTH - 1):
                    self.assertTrue(self.game.board[row][col].alive_next)
                elif(row == 0 and col == gol.BOARD_WIDTH - 1):
                    self.assertTrue(self.game.board[row][col].alive_next)
                elif(row == gol.BOARD_HEIGHT - 1 and col == 0):
                    self.assertTrue(self.game.board[row][col].alive_next)


if __name__ == "__main__":
    unittest.main()
        