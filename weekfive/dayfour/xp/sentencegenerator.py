

def get_words_from_file(my_file):
    with open(my_file, 'r+') as word_file:
        return map(str.rstrip, word_file.readlines())

print(get_words_from_file('sowpods.txt'))