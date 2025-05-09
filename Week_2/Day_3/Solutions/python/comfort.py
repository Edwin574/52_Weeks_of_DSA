class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_valid_index(string, index):
            skip = 0
            while index >= 0 :
                if string[index] == "#":
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    return index
                index -= 1
            return -1
        
        i , j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            i = get_valid_index(s , i)
            j = get_valid_index(t , j)

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False

            if (i >= 0) != (j >= 0):
                return False
            
            i -= 1
            j -= 1
        return True       