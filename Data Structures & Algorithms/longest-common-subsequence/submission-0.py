class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #back2backswe vid
        #start from end of biggest strings
        # if they both match we chop both off and add 1 to the total longest
        # if not we take the max of chopping one off from each
        # the table is beautiful!

        #string1 = the rows
        #string2 = the cols

        #   _ hello
        # -
        # w
        # o
        # r
        # l
        # d
        # you built it from top left to bottom right
        # either take turns choping 1 and take max if dont match
        # or if they match chop both and add 1
        ans = 0
        dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]
        print(dp)
        for r in range(1, len(text2) + 1):
            for c in range(1, len(text1) + 1):
                if text2[r-1] == text1[c-1]:
                    dp[r][c] = 1 + dp[r-1][c-1]
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])

        return dp[-1][-1]



        