import math
class IsPalindrome():
    def __init__(self, word):
        self.word = word

    def __call__(self):
        half_length = math.floor(len(self.word) / 2)
        for i in range(half_length):
            if self.word[i] != self.word[-i - 1]: #has to be -1 because end index starts from 1 and start index starts from 0
                return "Not a palindrome"
        return "Word is a palindrome"       

pal1 = IsPalindrome('radar')
print(pal1())