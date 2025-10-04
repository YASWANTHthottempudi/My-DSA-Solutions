class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, index):
            if index == len(word):
                return True
            if (row < 0 or row == len(board) or
                col < 0 or col == len(board[0]) or
                board[row][col] != word[index]):
                return False
            temp = board[row][col]
            board[row][col] = ' '
            # Explore all four directions
            found = (backtrack(row+1, col, index+1) or
                     backtrack(row-1, col, index+1) or
                     backtrack(row, col+1, index+1) or
                     backtrack(row, col-1, index+1))
            board[row][col] = temp
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False
