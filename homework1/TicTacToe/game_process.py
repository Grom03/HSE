from board import Board

class GameProcess:
    def __init__(self, test=False, size=None, now=None):
        start = 0
        if not test:
            self.size = int(input("Добро пожаловать в игру Крестики-Нолики! Для начала введите размер поля: "))
            if self.size < 3:
                raise Exception("Некорректный размер")
            start = int(input("Введите 1, если хотите начать игру и 2 иначе: "))
            if start == 1:
                self.player = 'X'
            else:
                self.player = 'O'
        else:
            self.size = size
            start = now

        if start == 1:
            self.player = 'X'
        else:
            self.player = 'O'
        self.now = 'X'
        self.board = Board(self.size)
        self.winner = None
        self.board.draw_board()

    def change_person(self):
        if self.now == 'X':
            self.now = 'O'
        else:
            self.now = 'X'

    def end_of_the_game(self):
        return self.winner is not None

    def make_player_turn(self, pos):
        self.board.update_board(pos, self.now)
        self.change_person()
        self.winner = self.board.is_winner(pos)

    def get_available_moves(self):
        return self.board.available_moves()

    def find_best_move(self, current_situation, depth=1):
        if depth == 5:
            return 0, -1
        pos = -1
        best_move = None
        available_moves = self.get_available_moves()
        for i in available_moves:
            self.board.update_board(i, current_situation)
            win = self.board.is_winner(i)
            if win is not None:
                self.board.step_back(i)
                if win == 'D':
                    return 0, i
                if current_situation == self.player:
                    return -10, i
                else:
                    return 10, i
            next, _ = self.find_best_move('X' if current_situation == 'O' else 'O', depth + 1)
            self.board.step_back(i)
            if best_move is None:
                best_move = next
                pos = i
            elif current_situation == self.player and best_move > next:
                best_move = next
                pos = i
            elif current_situation != self.player and best_move < next:
                best_move = next
                pos = i
        return best_move if best_move is not None else 0, pos

    def make_ai_turn(self):
        _, pos = self.find_best_move(self.now)
        self.board.update_board(pos, self.now)
        self.change_person()
        self.winner = self.board.is_winner(pos)
        self.board.draw_board()
