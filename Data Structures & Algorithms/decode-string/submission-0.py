class Solution:
    def decodeString(self, s: str) -> str:
        # use a stack
       # have 1 stack for strings
       # 1 stack for counts
       # maintain a curr string and a multiplier k
       # If it's a digit, update k = k * 10 + digit.
        # If it's [, push cur and k onto their respective stacks, then reset cur to empty and k to 0.
        # If it's ], pop the previous string and count. Set cur to the popped string plus the current string repeated by the popped count.
        # Otherwise, append the character to cur.
        # o(n+N)
        # the stacks are basically memory for what you were doing before entering [.

        #if digit:
        #     build the number

        # elif "[":
        #     save everything
        #     reset

        # elif "]":
        #     restore everything
        #     multiply current string

        # else:
        #     add the letter
        string_stack = []
        count_stack = []
        cur = ""
        k = 0

        for c in s:
            if c.isdigit(): # is part of a number multiplier
                k = k * 10 + int(c)
            elif c == "[": # need to start a new sequence
                string_stack.append(cur)
                count_stack.append(k)
                cur = ""
                k = 0
            elif c == "]": # need to form the multiplied sequence
                temp = cur # what im currently working on thats about to get multiplied out
                cur = string_stack.pop() # the thing we have saved in memory - we are tacking our nested one onto this
                count = count_stack.pop()
                cur += temp * count
            else: # a letter
                cur += c

        return cur