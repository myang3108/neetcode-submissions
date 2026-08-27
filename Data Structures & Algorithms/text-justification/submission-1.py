class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        i = 0
        n = len(words)
        
        while i < n:
            # --- Phase A: Greedy Packing ---
            line = []
            length = 0  # sum of word lengths
            while i < n and length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1
            
            # --- Phase B: Line Formatting ---
            # Case 1 (Last Line) & Case 2 (Single-word Line)
            if i == n or len(line) == 1:
                res.append(" ".join(line).ljust(maxWidth))
            else:
                # Case 3: Normal fully-justified line
                total_spaces = maxWidth - length
                gaps = len(line) - 1
                space_per_gap = total_spaces // gaps
                extra = total_spaces % gaps
                
                # Distribute the remainder spaces to the leftmost words
                for k in range(extra):
                    line[k] += " "
                
                res.append((" " * space_per_gap).join(line))
                
        return res