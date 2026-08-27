class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # need 4 directional loops - right down left up
        # keep track of 4 pointers -> start, end row and col
        sr = 0
        er = len(matrix) - 1
        sc = 0
        ec = len(matrix[0]) - 1
        ans = []

        while (sr <= er and sc <= ec):

            # ALWAYS MODIFY THE THING THAT WE CURRENTLY ARE WORKING ON.

            # first go right. add sr by 1 for next time 
            for c in range(sc, ec + 1):
                ans.append(matrix[sr][c])
            sr += 1

            # then go down and shrunk ec by 1 for next time
            for r in range(sr, er + 1):
                ans.append(matrix[r][ec])
            ec -= 1

            if (sr <= er and sc <= ec):
                # then go left and reduce er by 1 for next time
                for c in range(ec, sc - 1, -1):
                    ans.append(matrix[er][c])
                er -= 1

                # then go up and add sc by 1 for next time
                for r in range(er, sr - 1, -1):
                    ans.append(matrix[r][sc])
                sc += 1


        return ans
