import string
alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)

def userCypher(message, shift, encrypt_or_decrypt):
    cyphered_message = ''
    extra_chars = [' ', ',', '.', '!', "'"]
    for letter in message:
        if letter in extra_chars:
            cyphered_message += letter
        else :
            upper_or_lower = alphabet_upper if letter.isupper() else alphabet_lower
            index_of_letter = upper_or_lower.index(letter) 
            if encrypt_or_decrypt == 'encrypt' :
                cyphered_message += upper_or_lower[index_of_letter - shift]
            else :
                if index_of_letter >= 26 - shift: 
                    new_index = index_of_letter + shift - 26
                    cyphered_message += upper_or_lower[new_index]
                else :
                    cyphered_message += upper_or_lower[index_of_letter + shift]
    return cyphered_message

def getCypherInfo():
    message = input("What is your message?")
    encrypt_or_decrypt = ""
    shift = 0
    while True:
        encrypt_or_decrypt = input('Would you like to encrypt or decrypt?')
        if encrypt_or_decrypt == 'encrypt' or encrypt_or_decrypt == 'decrypt':
            break
    while shift == 0:
        shift = int(input('Choose amount to shift the letters'))

    cypher_message = userCypher(message, shift, encrypt_or_decrypt)
    print(f"Here's your {encrypt_or_decrypt}ed message: {cypher_message}")
    
getCypherInfo()