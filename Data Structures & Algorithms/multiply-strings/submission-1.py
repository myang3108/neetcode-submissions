class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # num1 has length m, num2 has length n the answer can have at most: m + n digits
        res = [0] * (len(num1) + len(num2))
        # for 123 * 45 -> res = [0,0,0,0,0]
        # 123 - i
        # 45  - j
        # carry = i+j
        # digit = i + j + 1
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                product = int(num1[i]) * int(num2[j])

                p1 = i + j # carry position
                p2 = i + j + 1 # actual digit

                total = product + res[p2]

                res[p2] = total % 10 # ones digit
                res[p1] += total // 10 # carry digit

        # remove leading 0
        if res[0] == 0:
            res = res[1:]

        return "".join(map(str, res))