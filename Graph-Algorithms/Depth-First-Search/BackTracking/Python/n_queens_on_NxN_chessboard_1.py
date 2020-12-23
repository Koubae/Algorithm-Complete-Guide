"""N queens on NxN chessboard 1"""

N = 4
board = [[0] * N for _ in range(N)]  # FAQ: Chessboard  NxN Matrix | Init all with 0


def init_n_queen():

    def check_queen_position(i, j):

        for k in range(0, N):  # FAQ: Checks Entire Row or Column for any queens
            if board[i][k] == 1 or board[k][j] == 1:
                return True

        for k in range(0, N):  # FAQ: 1 Checks Diagonal , see Footnotes for more details
            for l in range(0, N):
                if (k + l == i + j) or (k - l == i - j):
                    if board[k][l] == 1:
                        return True
        return

    def backtracking(queens_num):
        if not queens_num:
            return True
        else:
            for i in range(0, N):
                for j in range(0, N):

                    if (not (check_queen_position(i, j))) and (board[i][j] != 1):
                        board[i][j] = 1
                        if backtracking(queens_num - 1):
                            return True
                        else:
                            board[i][j] = 0

        return

    backtracking(N)
    return board


if __name__ == '__main__':
    for row in init_n_queen():
        print(row)

# FAQ:1 Checks Lef or Right Diagonals | Addition are Right Top to Left Bottom | Subtractions are Left Top  Right Bottom
# FAQ: (k-l == i-j)   \
#                      \
#                       \
#                        \

# FAQ: (k+l == i+j)     /
#                      /
#                     /
#                    /

