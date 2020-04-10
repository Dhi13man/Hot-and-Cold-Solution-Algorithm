from random import randint


class Game:
    def __init__(self, l_limit, u_limit, p_limit):
        print('\tHOT and COLD')
        print('A guessing game')
        print("\nI am thinking of a number between " + str(l_limit) + " and " + str(u_limit))
        print('Guess a number!!!!!\n')
        self.play_limit = p_limit
        self.ll, self.ul = l_limit, u_limit
        self.num = randint(l_limit, u_limit)
        self.guesses = []

    def check(self, guess):
        # WTF Human
        if guess < self.ll or guess > self.ul:
            print('OUT OF BOUNDS! Please try again: ')  # for user to see
            return 99  # for algorithm to see

        self.guesses.append(guess)

        # Loss state
        if len(self.guesses) > self.play_limit:
            print('Game over. Sorry you lost. The number was {}'.format(self.num))  # for user to see
            return 0  # for algorithm to see

        # Win state
        elif guess == self.num:
            print('\nCONGRATULATIONS, YOU GUESSED IT IN ONLY {} GUESSES!!'.format(len(self.guesses)))
            print("Guesses were: " + str(self.guesses))
            return 1  # for algorithm to see

        if len(self.guesses) >= 2:
            if abs(self.num - guess) < abs(self.num - self.guesses[-2]):
                print('WARMER!')  # for user to see
                return +10  # for algorithm to see
            else:
                print('COLDER!')  # for user to see
                return -10  # for algorithm to see
        # First guess condition
        else:
            # WARM range is 10 for 100 elements, 100 for 1000 elements and so on
            if abs(self.num - guess) <= int((self.ul - self.ll + 1) / 10):
                print('WARM!')  # for user to see
                return +5  # for algorithm to see
            else:
                print('COLD!')  # for user to see
                return -5  # for algorithm to see


class UserSolve:
    def __init__(self, x):
        self.ask_user(x)

    def ask_user(self, game_obj):
        inp = int(input("The game thinks of a number between " + str(game_obj.ll) + " and " + str(game_obj.ul)
                        + "\nWhat is your guess?\n"))
        # Recursively call itself if Game is not over so user can input his values
        if game_obj.check(inp) not in [0, 1]:
            self.ask_user(game_obj)


class AlgorithmSolve:
    def __init__(self, x, ch):
        self.lower_try = x.ll
        self.upper_try = x.ul
        self.method = ch
        self.detection_range = int((x.ul - x.ll + 1) / 10)
        self.mid = int((self.lower_try + self.upper_try) / 2)
        self.algorithm_trial(x, 'none')
        self.temp = 0

    def get_response_from_game(self, game):
        # code for step by step display
        if self.method == 1 and (self.lower_try != game.ll or self.upper_try != game.ul):
            input('\n')
        # Start
        print("\nThe game thinks of a number between " + str(game.ll) + " and " + str(game.ul)
              + "\nWhat is your guess?")
        self.mid = int((self.lower_try + self.upper_try) / 2)
        print("Algorithm guesses " + str(self.mid))
        return game.check(self.mid)

    def algorithm_lost(self, game_obj):
        print("\nAlgorithm loses. Pseudo randomness was too powerful.")
        print("The difference was:\t" + str(abs(self.mid - game_obj.num)))
        print("Error:\t%lf" % (abs(self.mid - game_obj.num) / (self.detection_range * 10) * 100) + " %")

    # When first try leads to Warm output
    def warm_algorithm(self, game_obj, last_change):
        game_response = self.get_response_from_game(game_obj)

        # End conditions:
        if game_response == 1:
            print("\nAlgorithm wins")
            return
        elif game_response == 0:
            self.algorithm_lost(game_obj)
            return

        # Mid game checks
        elif game_response == -10:
            # Punish behavior
            if last_change == 'upper':
                #  Last shift was to upper limit, shift lower limit right to mid
                self.upper_try = self.temp
                self.temp = self.lower_try
                self.lower_try = self.mid
                self.warm_algorithm(game_obj, 'lower')
            elif last_change == 'lower':
                #  Last shift was to lower limit, shift upper limit left to mid
                self.lower_try = self.temp
                self.temp = self.upper_try
                self.upper_try = self.mid
                self.warm_algorithm(game_obj, 'upper')
        elif game_response == +10:
            # Reward behavior
            if last_change == 'upper':
                # Last shift was upper limit leftward to mid, do again
                self.temp = self.upper_try
                self.upper_try = self.mid
                self.warm_algorithm(game_obj, 'upper')
            elif last_change == 'lower':
                # Last shift was lower limit rightward to mid, do again
                self.temp = self.lower_try
                self.lower_try = self.mid
                self.warm_algorithm(game_obj, 'lower')

    def algorithm_trial(self, game_obj, last_change):
        game_response = self.get_response_from_game(game_obj)

        # End conditions:
        if game_response == 1:
            print("\nAlgorithm wins")
            return
        elif game_response == 0:
            self.algorithm_lost(game_obj)
            return

        # First check:
        elif game_response == 5:  # Luckiest case. Decrease sample size to WARM zone(detection range)
            self.temp = self.mid + self.detection_range * 2
            self.lower_try = self.mid - self.detection_range * 2
            self.upper_try = self.mid
            self.warm_algorithm(game_obj, 'upper')
        elif game_response == -5:
            self.temp = self.lower_try
            self.lower_try = self.mid
            self.algorithm_trial(game_obj, 'lower')

        # Mid game checks
        # Punish behavior
        elif game_response == -10:
            if last_change == 'lower':  # Lower limit change last, try changing upper instead
                self.lower_try = self.temp
                self.temp = self.upper_try
                self.upper_try = self.mid
                self.algorithm_trial(game_obj, 'upper')
            elif last_change == 'upper':  # Upper limit change last, try changing lower instead
                self.upper_try = self.temp
                self.temp = self.lower_try
                self.lower_try = self.mid
                self.algorithm_trial(game_obj, 'lower')
        # Reward Behavior
        elif game_response == 10:  # Lower limit change last, do again
            if last_change == 'lower':
                self.temp = self.lower_try
                self.lower_try = self.mid
                self.algorithm_trial(game_obj, 'lower')
            elif last_change == 'upper':  # Upper limit change last, do again
                self.temp = self.upper_try
                self.upper_try = self.mid
                self.algorithm_trial(game_obj, 'upper')


# Main code starts here
if __name__ == '__main__':
    upper = 100
    lower = 0
    chances = 10
    g1 = Game(lower, upper, chances)  # Upper Limit, Lower Limit of random range, how many chances given to player
    choice = int(input("Enter  0 for Auto-solve, 1 to attempt on your own: "))
    if choice == 1:
        u = UserSolve(g1)
        choice = int(input("Enter  0 for giving Algorithm a chance to solve, 1 to exit: "))
    if choice == 0:
        choice = int(input("\nEnter 0 for Instant solution, 1 for Step by step solution: "))
        a = AlgorithmSolve(g1, choice)
