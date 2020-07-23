from random import choice

def get_words_from_file(my_file):
    with open(my_file, 'r+') as word_file:
        return [word.rstrip() for word in word_file.readlines()]

def get_random_sentence(sentence_length, word_array):
    my_sentence = ''
    for i in range(sentence_length):
        my_sentence += f'{choice(word_array)} '
    return my_sentence.lower()

def main():
    print('We will create a random sentence with a number of words of your choosing')
    try:
        sentence_length = int(input('How many words would you like in your sentence? (2-20)'))
        if 2 <= sentence_length <= 20:
            words = get_words_from_file('sowpods.txt')
            generated_sentence = get_random_sentence(sentence_length, words)
            print(generated_sentence)
        else:
            print('Invalid number')
            return
    except ValueError:
        print('The sentence generator only accepts integers')

main()