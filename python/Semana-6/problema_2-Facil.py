class Solution:
    def isPalindrome(self, x: int) -> bool:
        xs= str(x)
        if xs.isdigit():
            return int(xs[::-1]) - x == 0
        else:
            return False



# Version mejorada:

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]