import game

def get_user_menu_choice():
    return input('''Menu:
    (g) Play a new game
    (x) Show scores and exit
    ''')

def print_results(results):
    print(f'''Game Results:
    You won {results['win']} times
    You lost {results['lose']} times
    You drew {results['draw']} times
    
    Thanks for playing!''')

def main():
    my_game = game.Game()
    results = {'win': 0, 'lose': 0, 'draw': 0}
    while True:
        choice = get_user_menu_choice()
        if choice == 'g':
            result = my_game.play()
            results[result] += 1
        elif choice == 'x':
            print_results(results)
            break

main()