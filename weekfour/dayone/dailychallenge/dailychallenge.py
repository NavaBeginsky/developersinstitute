user_string = input('Give me a string')
print(f'The first character is {user_string[0]}')
last_pos_user_string = len(user_string) - 1
print(f'The last character is {user_string[last_pos_user_string]}')
build_string = ' '
for i in user_string:
    build_string = build_string + i
    print(build_string)

import random
string_to_list = list(user_string)
random.shuffle(string_to_list)
final_string = ''.join(string_to_list)
print(final_string)