from unittest import TestCase, main
from main_tictactoe import game
from board import Board

class UnitTests(TestCase):
    def test_correct_draw(self):
        self.assertEquals(Board(5).make_board(), "-----------------------------------------\n"
                                                 "|   1   |   2   |   3   |   4   |   5   |\n"
                                                 "-----------------------------------------\n"
                                                 "|   6   |   7   |   8   |   9   |   10  |\n"
                                                 "-----------------------------------------\n"
                                                 "|   11  |   12  |   13  |   14  |   15  |\n"
                                                 "-----------------------------------------\n"
                                                 "|   16  |   17  |   18  |   19  |   20  |\n"
                                                 "-----------------------------------------\n"
                                                 "|   21  |   22  |   23  |   24  |   25  |\n"
                                                 "-----------------------------------------\n")

    def test_minimax_3x3(self):
        self.assertEquals(game(True, 3, 1, [5, 2, 7, 6, 9]),
                          "It's Draw!\n"
                          "-------------------------\n"
                          "|   O   |   X   |   O   |\n"
                          "-------------------------\n"
                          "|   O   |   X   |   X   |\n"
                          "-------------------------\n"
                          "|   X   |   O   |   X   |\n"
                          "-------------------------\n")
    def test_common(self):
        board = Board(3)
        self.assertEquals(board.make_board(), "-------------------------\n"
                                              "|   1   |   2   |   3   |\n"
                                              "-------------------------\n"
                                              "|   4   |   5   |   6   |\n"
                                              "-------------------------\n"
                                              "|   7   |   8   |   9   |\n"
                                              "-------------------------\n")
        board.update_board(2, 'X')
        self.assertEquals(board.make_board(), "-------------------------\n"
                                              "|   1   |   X   |   3   |\n"
                                              "-------------------------\n"
                                              "|   4   |   5   |   6   |\n"
                                              "-------------------------\n"
                                              "|   7   |   8   |   9   |\n"
                                              "-------------------------\n")
        board.update_board(3, 'X')
        self.assertEquals(board.make_board(), "-------------------------\n"
                                              "|   1   |   X   |   X   |\n"
                                              "-------------------------\n"
                                              "|   4   |   5   |   6   |\n"
                                              "-------------------------\n"
                                              "|   7   |   8   |   9   |\n"
                                              "-------------------------\n")
        board.update_board(1, 'O')
        self.assertEquals(board.make_board(), "-------------------------\n"
                                              "|   O   |   X   |   X   |\n"
                                              "-------------------------\n"
                                              "|   4   |   5   |   6   |\n"
                                              "-------------------------\n"
                                              "|   7   |   8   |   9   |\n"
                                              "-------------------------\n")
        self.assertEquals(board.is_winner(1), None)
        board.step_back(1)
        self.assertEquals(board.make_board(), "-------------------------\n"
                                              "|   1   |   X   |   X   |\n"
                                              "-------------------------\n"
                                              "|   4   |   5   |   6   |\n"
                                              "-------------------------\n"
                                              "|   7   |   8   |   9   |\n"
                                              "-------------------------\n")
        board.step_back(2)
        self.assertEquals(board.make_board(), "-------------------------\n"
                                              "|   1   |   2   |   X   |\n"
                                              "-------------------------\n"
                                              "|   4   |   5   |   6   |\n"
                                              "-------------------------\n"
                                              "|   7   |   8   |   9   |\n"
                                              "-------------------------\n")
        board.update_board(2, 'X')
        board.update_board(1, 'X')
        self.assertEquals(board.make_board(), "-------------------------\n"
                                              "|   X   |   X   |   X   |\n"
                                              "-------------------------\n"
                                              "|   4   |   5   |   6   |\n"
                                              "-------------------------\n"
                                              "|   7   |   8   |   9   |\n"
                                              "-------------------------\n")
        self.assertEquals(board.is_winner(1), 'X')

if __name__ == "__main__":
    main()