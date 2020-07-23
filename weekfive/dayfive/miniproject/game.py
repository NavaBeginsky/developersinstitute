from random import choice


class Game():

    def get_user_item(self):
        while True:
            player_choice = input(
                'Would you like to play "rock", "paper", or "scissors"?')
            if player_choice == 'rock' or player_choice == 'scissors' or player_choice == 'paper':
                return player_choice
            else:
                print('Please choose a valid option.')

    def get_computer_item(self):
        return choice(['rock', 'paper', 'scissors'])

    def get_game_result(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return 'draw'
        if player_choice == 'rock':
            if computer_choice == 'paper':
                return 'lose'
            if computer_choice == 'scissors':
                return 'win'

        if player_choice == 'paper':
            if computer_choice == 'scissors':
                return 'lose'
            if computer_choice == 'rock':
                return 'win'

        if player_choice == 'scissors':
            if computer_choice == 'rock':
                return 'lose'
            if computer_choice == 'paper':
                return 'win'

    def play(self):
        player_choice = self.get_user_item()
        computer_choice = self.get_computer_item()
        result = self.get_game_result(player_choice, computer_choice)
        print(
            f'You selected {player_choice}. The computer played {computer_choice}. You {result}.')
        return result
