class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowZero = False
        # find which rows/cols need to be zeroed
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    
                    # dont do it for the top left
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        rowZero = True
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # zero outfirst col
        if matrix[0][0] == 0: 
            for r in range(len(matrix)):
                matrix[r][0] = 0
        
        if rowZero == True: 
            for col in range(len(matrix[0])):
                matrix[0][col] = 0

                