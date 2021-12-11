from random import randint
from math import sqrt

class person:
    def __init__(self, x, y):
        self.x = randint(1, 100)
        self.y = randint(1, 100)

    Susceptable = True
    Infected = False
    Recovered = False

    daysInfected = 0

    # check if person gets infected
    def is_infected(self, others, ROI):
        for i in range(len(others)):
            if self.Susceptable == True:
                distance = sqrt((self.y - others[i].y)**2 + (self.x - others[i].x)**2)
                if distance <= ROI:
                    if randint(1, 6) == 1:
                        self.Infected = True

    def is_recovered(self, recovery):
        if self.daysInfected == recovery:
            self.Susceptable = False
            self.Recovered = True

    def change_pos(self):
        pass
