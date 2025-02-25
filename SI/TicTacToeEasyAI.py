from easyAI import TwoPlayerGame
from easyAI.Player import Human_Player
from easyAI import TranspositionTable, solve_with_iterative_deepening

class TicTacToe(TwoPlayerGame):
    """The board positions are numbered as follows:
    1 2 3
    4 5 6
    7 8 9
    """

    def __init__(self, players = None):
        self.players = players
        self.board = [0 for i in range(9)]
        self.current_player = 1  # player 1 starts.

    def possible_moves(self):
        return [i + 1 for i, e in enumerate(self.board) if e == 0]

    def make_move(self, move):
        self.board[int(move) - 1] = self.current_player

    def unmake_move(self, move):  # optional method (speeds up the AI)
        self.board[int(move) - 1] = 0

    def lose(self):
        """ Has the opponent "three in line ?" """
        return any(
            [
                all([(self.board[c - 1] == self.opponent_index) for c in line])
                for line in [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],  # horiz.
                    [1, 4, 7],
                    [2, 5, 8],
                    [3, 6, 9],  # vertical
                    [1, 5, 9],
                    [3, 5, 7],
                ]
            ]
        )  # diagonal

    def is_over(self):
        return (self.possible_moves() == []) or self.lose()

    def show(self):
        print(
            "\n"
            + "\n".join(
                [
                    " ".join([[".", "O", "X"][self.board[3 * j + i]] for i in range(3)])
                    for j in range(3)
                ]
            )
        )

    def scoring(self):
        return -100 if self.lose() else 0


if __name__ == "__main__":

    from easyAI import AI_Player, Negamax, SSS, DUAL
    tt = TranspositionTable()
    TicTacToe.ttentry = lambda game : game.board
    r, d, m = solve_with_iterative_deepening(game = TicTacToe(), ai_depths=range(2,20), win_score=100, tt = tt)
    ai_algo1 = SSS(10)
    ai_algo2 = Negamax(5)
    game = TicTacToe([AI_Player(tt), Human_Player()])
    game.play()
    # for i in history:
    #     try:
    #         print(f'Zagrano {i[1]}')
    #     except:
    #         print("Koniec")