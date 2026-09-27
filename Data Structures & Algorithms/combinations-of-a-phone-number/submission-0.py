class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # need to make a decision tree -> are we done with the digit yet -> need to go through all of the options for that digit before we move onto the next digit -> each layer is the digit we are working on

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def helper(curr, idx): # take in the current path and index of the digit we r working on
            if idx == len(digits): # got through to the end
                res.append(curr[:])
                return
             
            # now for each letter in the current digit we add it to our path and then recurse and then remove
            for letter in phone[digits[idx]]:
                # add the curr letter to our string and then remove after
                curr += letter
                helper(curr, idx + 1)
                curr = curr[:-1]
        if digits:
            helper("", 0)
        return res