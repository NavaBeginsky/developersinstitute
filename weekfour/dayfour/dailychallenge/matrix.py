import string
alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase

matrix_list = [
    [7, ' ', 3],
    ['T','s','i'],
    ['h','%','x'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['i', 'r', '!']
]    

def decodeMatrix(matrix, items_per_list):
    ''' This function loops the amount of times passed in to the items per list parameter. Within that loop it goes through each 
    list within the matrix passed in and gets the character in index 0. If the character is a letter, it adds it to the decoded
    word string, if it is a different kind of character it adds a space if there wasn't already a space and if it's a number it
    skips it. It then increases the index and continues until it's gone through the whole thing. Function returns the decoded matrix '''
    decoded_words = ''
    i = 0
    while i < items_per_list :
        for char in matrix:
            try :
                if char[i] in alphabet_lower or char[i] in alphabet_upper:
                    decoded_words += char[i]
                else :
                    if decoded_words[-1] == ' ' or char[i] == ' ':
                        pass
                    else :
                        decoded_words += ' '
            except :
                if char[i] is int :
                    pass
        i += 1
            
    return decoded_words

print(decodeMatrix(matrix_list, 3))

