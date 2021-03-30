import random

# problem 1.a
class Months:
    def __init__(self):
        self.month = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'December')

    def PiDay(self):
        pi_day = self.month[2]
        print(pi_day);

#problem 1.b
    def BdayLocations(self):
        locations = ['New York', 'LA', 'Florida']
        locations.append("Georgia")
        for location in locations:
            print(location)

#problem 1.c


    def SweepstakesContestants(self):
        self.winner = None
        self.contestants = {1: Contestant("Rob"), 2: Contestant("Rob S"), 3: Contestant("Nevin")}

    def get_winner(self):
        self.winner =self.contestants[random.randint(1, 4)]
        print(self.winner)




months= Months().PiDay()