class NQueensBranchAndBound:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.solutions = []

    def solve(self):
        self.backtrack(0)
        return self.solutions

    def backtrack(self, col):
        if col == self.n:
            self.add_solution()
            return

        for row in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.backtrack(col + 1)
                self.board[row][col] = 0

    def is_safe(self, row, col):
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        for i, j in zip(range(row, self.n), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def add_solution(self):
        solution = []
        for row in self.board:
            solution.append("".join("Q" if cell == 1 else "-" for cell in row))
        self.solutions.append(solution)
n = 4  # Number of queens
solver = NQueensBranchAndBound(n)
solutions = solver.solve()
for solution in solutions:
    print('\n'.join(solution))
    print()
