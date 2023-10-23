class Palindrome:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]: # x[::-1] reverses a string
            return True
        else:
            return False