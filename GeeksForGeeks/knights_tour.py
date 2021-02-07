'''If all squares are visited 
    print the solution
Else
   a) Add one of the next moves to solution vector and recursively 
   check if this move leads to a solution. (A Knight can make maximum 
   eight moves. We choose one of the 8 moves in this step).
   b) If the move chosen in the above step doesn't lead to a solution
   then remove this move from the solution vector and try other 
   alternative moves.
   c) If none of the alternatives work then return false (Returning false 
   will remove the previously added item in recursion and if false is 
   returned by the initial call of recursion then "no solution exists" )

Fill out the board with an increment of numbers (counting moves really).
The point of this is to exercise backtracking. So if the "move" method
  iterates over the board but breaks the rules, fail and try again.
Finally, return "no solution" if the last of the valid moves fails.
*We iterate over valid moves
'''
import copy



class KnightsTour:
    def __init__(self, board):
        self.board = board
        self.edge_high = len(self.board)
        self.edge_low = -1
        self.vm = 8 # number of possible moves

    def valid_moves(self, vm, i, j):
        # RR/D - RR/U - LL/D - LL/U
        # DD/L - DD/R - UU/L - UU/R
        moves = {
            0 : (i+2, j+1), # DD/R
            1 : (i-2, j+1), # UU/R
            2 : (i+1, j-2), # LL/D
            3 : (i-1, j+2), # RR/U
            4 : (i-2, j-1), # UU/L
            5 : (i+2, j-1), # DD/L
            6 : (i+1, j+2), # RR/D
            7 : (i-1, j-2)  # LL/U
            }

        return moves[vm]

    def finished(self):
        fin = True
        for x in self.board:
            if None in x:
                fin = False
                break
        return fin

    def is_avail(self, i, j):
        try:
            if self.board[i][j] is None:
                return True
        except IndexError:
            return False

    def board_util(self, i, j, next_int):
        if self.finished(): return True

        # I/J is the current vector
        # NI/NJ is the future vector
        for vm in range(self.vm):
            move = self.valid_moves(vm, i, j)
            ni, nj = move[0], move[1]
            #print(f"...executing int {next_int} for {ni, nj}")
            if self.is_avail(ni, nj):
                self.board[ni][nj] = next_int
                if self.board_util(ni, nj, next_int + 1):
                    return True
                self.board[ni][nj] = None
        return False

    def solve(self):
        # Initialize
        self.board[0][0] = 0
        if not self.board_util(0, 0, 1):
            return "No solution found"
        return self.board
 


if __name__ == "__main__":
    board = [ [None for y in range(8)] for x in range(8) ]
    k = KnightsTour(board)
    print(k.solve())
