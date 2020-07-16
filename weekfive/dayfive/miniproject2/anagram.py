from collections import Counter

class AnagramChecker():
    def __init__(self):
        with open('sowpods.txt') as my_file:
           self.words_file = my_file.read() 

    def is_valid_word(self, word):
        return True if word in self.words_file else False
    
    def get_anagrams(self, word):
        letter_count = Counter(word)
        print(letter_count)

ag = AnagramChecker()
ag.get_anagrams('princess')