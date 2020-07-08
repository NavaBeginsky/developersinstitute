def display_message():
    print("I am learning about functions in this chapter")

display_message()

#exercise 2
def favorite_book(title):
    print(f"One of my favorite books is {title}")
favorite_book('Harry Potter')

#exercise 3
def make_shirt(size = 'large', text = 'I love Python'):
    print(f'The size of the shirt is {size} and {text} will be printed on it.')

make_shirt('large', 'Kale Yeah!')
make_shirt(text = 'Bitch, Peas', size = 'small')

make_shirt()
make_shirt('medium')
make_shirt(text = 'Message 2')

#exercise 4
magician_names = ['houdini', 'david blane', 'criss angel']

def show_magicians(magicians):
    for name in magicians:
        print(name)

def make_great(*magicians):
    for name in magicians:
        print(name)
        # name = "The Great" + name

make_great(magician_names)
# show_magicians(magician_names)

