class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # need a visited grid for similation - know when to change dir
        # check if next one in bounds
        # have 4 directions (similar to rotting oranges)

        sc = 0
        sr = 0
        ec = len(matrix[0]) - 1
        er = len(matrix) - 1
        ans = []

        while (sr <= er and sc <= ec):
            for c in range(sc, ec + 1):
                ans.append(matrix[sr][c])
            sr += 1

            for r in range(sr, er + 1):
                ans.append(matrix[r][ec])
            ec -= 1

            if (sr <= er and sc <= ec):
                for c in range(ec, sc - 1, -1):
                    ans.append(matrix[er][c])
                er -= 1
            
            if (sr <= er and sc <= ec):
                for r in range(er, sr - 1, -1):
                    ans.append(matrix[r][sc])
                sc += 1
        
        return ans


        