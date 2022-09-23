class Board:
    def __init__(self, size):
        self.size = size
        self.board = [str(i + 1) for i in range(size * size)]
        self.left_fields = size * size

    def make_board(self):
        out = '-' * (8 * self.size + 1) + '\n'
        for i in range(self.size):
            for j in range(self.size):
                if len(self.board[i * self.size + j]) == 1:
                    out += "|   " + self.board[i * self.size + j] + "   "
                elif len(self.board[i * self.size + j]) == 2:
                    out += "|   " + self.board[i * self.size + j] + "  "
                else:
                    out += "|  " + self.board[i * self.size + j] + "  "
            out += "|\n" + ('-' * (8 * self.size + 1)) + '\n'
        return out

    def draw_board(self):
        print(self.make_board())

    def update_board(self, pos, val):
        if pos > 0 and pos <= self.size * self.size and self.board[pos - 1] != 'X' and self.board[pos - 1] != 'O':
            self.board[pos - 1] = val
            self.left_fields -= 1

    def step_back(self, pos):
        self.board[pos - 1] = str(pos)
        self.left_fields += 1

    def is_winner(self, pos):
        count_x = "X" * min(self.size, 5)
        count_o = "O" * min(self.size, 5)
        cur = ""
        for i in range(pos - (pos - 1) % self.size - 1, int((pos - 1) / self.size + 1) * self.size):
            cur += self.board[i]
        if count_x in cur:
            return 'X'
        if count_o in cur:
            return 'O'
        cur = ""
        for i in range(self.size):
            cur += self.board[pos % self.size - 1 + i * self.size]
        if count_x in cur:
            return 'X'
        if count_o in cur:
            return 'O'
        cur = ""
        cur_pos = pos - self.size - 1
        while cur_pos > 0:
            cur = self.board[cur_pos - 1] + cur
            cur_pos -= (self.size + 1)
        cur_pos = pos
        while cur_pos <= self.size * self.size:
            cur += self.board[cur_pos - 1]
            cur_pos += (self.size + 1)
        if count_x in cur:
            return 'X'
        if count_o in cur:
            return 'O'
        cur = ""
        cur_pos = pos
        while cur_pos > 0 and cur_pos % self.size != 1:
            cur = self.board[cur_pos - 1] + cur
            cur_pos -= (self.size - 1)
        cur_pos = pos + self.size - 1
        while cur_pos <= self.size * self.size and cur_pos % self.size != 0:
            cur += self.board[cur_pos - 1]
            cur_pos += (self.size - 1)
        if count_x in cur:
            return 'X'
        if count_o in cur:
            return 'O'
        if self.is_ended():
            return "D"
        return None

    def is_ended(self):
        return self.left_fields == 0

    def available_moves(self):
        moves = set()
        for i in range(self.size * self.size):
            if self.board[i] != 'X' and self.board[i] != 'O':
                moves.add(i + 1)
        return moves
