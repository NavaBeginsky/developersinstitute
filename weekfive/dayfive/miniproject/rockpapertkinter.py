from random import choice
import tkinter
root = tkinter.Tk()
root.title('Rock Paper Scissors')


class Game():
    game_options = ['rock', 'paper', 'scissors']

    def __init__(self, root):
        self.root = root
        self.start_button = tkinter.Button(
            root, text="Play", command=self.get_user_item)
        self.start_button.pack()
        self.choose_play_option = tkinter.Label(
            self.root, text='Would you like to play "rock", "paper", or "scissors"?')
        self.input_field = tkinter.Entry(self.root)
        self.current_choice = ''
        self.submit_button = tkinter.Button(
            self.root, text='Submit', command=self.assign_current_choice)
        self.error = tkinter.Label(
            self.root, text='Please choose a valid option.')
        self.game_button = tkinter.Button(
            root, text='Play a new game', command=self.get_user_item)
        self.exit_button = tkinter.Button(
            root, text='Show Scores and Exit', command=self.print_results)
        self.results = {'win': 0, 'lose': 0, 'draw': 0}
        self.current_round = 1

    def get_user_item(self):
        if self.current_round > 1:
            self.result_label.pack_forget()
            self.game_button.pack_forget()
            self.exit_button.pack_forget()
        else:
            self.start_button.pack_forget()
        self.choose_play_option.pack()
        self.input_field.pack()
        self.submit_button.pack()

    def assign_current_choice(self):
        self.choose_play_option.pack_forget()
        self.input_field.pack_forget()
        self.submit_button.pack_forget()
        self.current_choice = self.input_field.get()
        if self.current_choice not in self.game_options:
            self.error.pack()
            self.get_user_item()
        else:
            self.error.pack_forget()
            self.play()

    def get_computer_item(self):
        return choice(self.game_options)

    def get_game_result(self, computer_choice):
        if self.current_choice == computer_choice:
            return 'draw'
        if self.current_choice == 'rock':
            if computer_choice == 'paper':
                return 'lose'
            if computer_choice == 'scissors':
                return 'win'
        if self.current_choice == 'paper':
            if computer_choice == 'scissors':
                return 'lose'
            if computer_choice == 'rock':
                return 'win'
        if self.current_choice == 'scissors':
            if computer_choice == 'rock':
                return 'lose'
            if computer_choice == 'paper':
                return 'win'

    def display_user_menu_choice(self):
        self.game_button.pack()
        self.exit_button.pack()

    def print_results(self):
        self.result_label.pack_forget()
        self.game_button.pack_forget()
        self.exit_button.pack_forget()
        results = tkinter.Label(root, text=f'''Game Results:
        You won {my_game.results['win']} times
        You lost {my_game.results['lose']} times
        You drew {my_game.results['draw']} times
        Thanks for playing!''')
        results.pack()

    def play(self):
        computer_choice = self.get_computer_item()
        result = self.get_game_result(computer_choice)
        self.result_label = tkinter.Label(
            self.root, text=f'You selected {self.current_choice}. The computer played {computer_choice}. You {result}.')
        self.result_label.pack()
        self.results[result] += 1
        self.current_round += 1
        self.display_user_menu_choice()


my_game = Game(root)
root.mainloop()
