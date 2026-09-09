class Solution:
    def trap(self, height: List[int]) -> int:
        # we need the max to its to the left, max to its right -> the minimum of those is the trapper
        # this represents the potenetial max -> need to subtract from the curr height to get the actual
        l_wall = 0
        r_wall = 0
        n = len(height)
        maxleft = [0] * n
        maxright = [0] * n

        for i in range(n):
            j = -i - 1
            maxleft[i] = l_wall
            maxright[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])

        total = 0

        for i in range(n):
            pot = min(maxleft[i], maxright[i])
            total += max(0, pot - height[i])
        
        return total