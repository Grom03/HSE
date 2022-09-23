from game_process import GameProcess

def game(test=False, size=None, now=None, moves=None):
    process = GameProcess(test, size, now)
    i = 0
    while not process.end_of_the_game():
        if process.player != process.now:
            process.make_ai_turn()
        else:
            if test:
                process.make_player_turn(moves[i])
                i += 1
            else:
                pos = int(input("Введите номер клетки, куда хотите сходить: "))
                process.make_player_turn(pos)
    process.board.draw_board()
    if process.winner == 'D':
        return "It's Draw!\n" + process.board.make_board()
    elif (process.winner == 'X' and process.player == 'X') or (process.winner == 'O' and process.player == 'O'):
        return "You win!\n" + process.board.make_board()
    else:
        return "Computer wins!\n" + process.board.make_board()

if __name__ == '__main__':
    print(game())

