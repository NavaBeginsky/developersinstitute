import string

english_stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']

class Text():
    def __init__(self, my_string):
        self.my_string = my_string
        self.word_quantities = {}
        for word in self.my_string.split(' '):
            if word == '': #it was counting extra white space as words
                pass
            elif word.lower() in self.word_quantities:
                self.word_quantities[word.lower()] +=1
            else :
                self.word_quantities[word.lower()] = 1
    
    def word_frequency(self, word):
        frequency = self.word_quantities[word]
        if frequency:
            return f"The word {word} appears {frequency} times"
        else:
            return None

    def most_common_word(self):
        most_common = ['', 0]
        for k, v in self.word_quantities.items():
            if v > most_common[1] and k not in english_stopwords:
                most_common = [k, v]
        return most_common[0]

    def unique_words(self):
        unique_words = [k for k, v in self.word_quantities.items() if v == 1]
        return unique_words
    
    @classmethod
    def return_text_instance(cls, file):
        with open(file, 'r') as file:
            file_to_my_string = file.read().replace('\n', ' ')
        return cls(file_to_my_string)
        
class TextModification(Text):
    def without_punctuation(self):
        translation_table = str.maketrans('', '', string.punctuation)
        return ''.join([letter.translate(translation_table) for letter in self.my_string])

    def without_stop_words(self):
        string_without_stopwords = ''
        for word in self.my_string.split(' '):
            if word not in english_stopwords:
                string_without_stopwords += f'{word} '
        return string_without_stopwords

    def without_special_chars(self):
        string_without_special_chars = ''
        for letter in self.my_string:
            if letter.isalnum() or letter == ' ':
                string_without_special_chars += letter
        return string_without_special_chars

my_file_text = Text.return_text_instance('C:\\Users\\navag\\Desktop\\developersinstitute\\weekfive\\dayfour\\dailychallenge\\text.txt')
print(my_file_text.most_common_word())