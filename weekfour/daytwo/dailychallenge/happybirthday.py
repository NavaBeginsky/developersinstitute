from datetime import datetime, timedelta
birthday = input('what is your birthday ex. DD/MM/YYYY')
birthday_convert_to_date = datetime.strptime(birthday, "%d/%m/%Y")
current_date = datetime.now()
age = int((current_date - birthday_convert_to_date) / 365 / timedelta (days=1))
age_to_string = str(age)
last_digit_of_age = int(age_to_string[-1])
candles = 'i' * int(last_digit_of_age)
print(f'''\t ___{candles}___ 
       | :H:a:p:p:y:  |
     __|______________|__
    |^^^^^^^^^^^^^^^^^^^^|
    | :B:i:r:t:h:d:a:y:  |
    |                    |
    ~~~~~~~~~~~~~~~~~~~~~~
    ''')
