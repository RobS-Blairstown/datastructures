import random
from contestants import Contestant


class SweepstakesWinner:
    def __init__(self):
        self.winner = None
        self.contestants = {1: Contestant("Rob"), 2: Contestant("Rob S"), 3: Contestant("Nevin")}

    def get_winner(self):
        self.winner = self.contestants[random.randint(1, 3)]
        print(self.winner)
