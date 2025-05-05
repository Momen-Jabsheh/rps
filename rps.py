import time
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']


"""The Player class is the parent class for all of the Players
in this game"""


def print_sleep(prompt, s_time):
    print(prompt)
    time.sleep(s_time)


class Player:
    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        while True:
            a = "what do you want to play('rock', 'paper', 'scissors')"
            q = input(a).lower()
            if q == "rock":
                return 'rock'
            elif q == "paper":
                return 'paper'
            elif q == "scissors":
                return 'scissors'
            else:
                print_sleep("try again", 1)


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        self.a2 = "rock"

    def learn(self, my_move, their_move):
        self.a1 = my_move
        self.a2 = their_move

    def move(self):
        return self.a2


class RockPlayer(Player):
    def move(self):
        return "rock"


class CyclePlayer(Player):
    def __init__(self):
        self.a1 = 'rock'

    def learn(self, my_move="rock", their_move="rock"):
        self.a1 = my_move
        self.a2 = their_move

    def move(self):
        i = moves.index(self.a1)
        return moves[(i + 1) % 3]


def beats(one, two):
    return (
        (one == 'rock' and two == 'scissors') or
        (one == 'scissors' and two == 'paper') or
        (one == 'paper' and two == 'rock')
    )


def player_chose_system():
    print_sleep(
        "Choose player type:\n"
        "1- Normal Player\n"
        "2- Random Player\n"
        "3- Reflect Player\n"
        "4- Cycle Player\n"
        "5- Human Player\n", 1
    )

    try:
        q = int(input("Choose the player type (1-5): "))
        if q < 1 or q > 5:
            print_sleep("Please choose a number between 1 and 5.", 1)
            return player_chose_system()
    except ValueError:
        print_sleep("Invalid input. Please enter a number.", 1)
        return player_chose_system()

    if q == 1:
        return RockPlayer()
    elif q == 2:
        return RandomPlayer()
    elif q == 3:
        return ReflectPlayer()
    elif q == 4:
        return CyclePlayer()
    elif q == 5:
        return HumanPlayer()
    else:
        return RockPlayer()


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.scorep1 = 0
        self.scorep2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_sleep("the first player :", 1)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            self.scorep1 += 1
            print(f"the winner is first player: {move1}")
        elif beats(move2, move1):
            self.scorep2 += 1
            print(f"the winner is second player {move2}")
        else:
            print("there is no winner this round")
        print(f"Current Score\nPlayer 1: {self.scorep1}"
              f"\nPlayer 2: {self.scorep2}")

    def play_game(self):
        print_sleep("Game start!", 1)
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        if self.scorep1 == self.scorep2:
            print_sleep("Game over!", 1)
            print_sleep("It's a tie!", 1)
        elif self.scorep1 > self.scorep2:
            print_sleep("the winner is the first player", 1)
        else:
            print_sleep("the winner is the second player", 1)
        print(f"score :\n first player: {self.scorep1}"
              f"\n second player {self.scorep2}")


if __name__ == '__main__':
    k1 = player_chose_system()
    k2 = player_chose_system()
    game = Game(k1, k2)
    game.play_game()
