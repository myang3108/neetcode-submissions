class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # dfs until it no longer matches the idx of the word
        # then backtrack and go in all the other directions
        rowsize = len(board)
        colsize = len(board[0])


        def dfs(r,c,i):
            # if the board[r][c] matches i -> do i+1 on each of the neighbors on the board
            # base case: if the r or c is out of bounds return false
            # if we reach the end of i return true -> len(word)
            # if current cell doesnt match i return false
            # need the mark the current squre as visited 
            print(r,c,i)
            if i >= len(word):
                return True
            if r < 0 or c < 0 or r >= rowsize or c >= colsize or board[r][c] != word[i] or board[r][c] == "visited":
                return False

            # need to mark this one as used and check the neighbors
            tmp = board[r][c]
            board[r][c] = "visited"
            if dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1):
                return True
            board[r][c] = tmp
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,0):
                    return True
        
        return False
            
