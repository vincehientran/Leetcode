import random

import scipy as sp

class Horse(object):
    def __init__(self, speed=9.7, jump=3.5, health=22.5):
        self.speed = speed
        self.jump = jump
        self.health = health

    def __lt__(self, other):
        return self.speed < other.speed

    def __gt__(self, other):
        return self.speed > other.speed

    def __eq__(self, other):
        return self.speed == other.speed

    def __repr__(self):
        return '\nSpeed: ' + str(self.speed) + '\nJump: ' + str(self.jump) + '\nHealth: ' + str(self.health)

    def __str__(self):
        return self.__repr__()


def breedAttemptsSpeed(horse1, horse2, speed=10):
    attempts = 1
    offspringSpeed = (horse1.speed + horse2.speed + random.uniform(4.86, 14.57)) / 3
    offspringJump = (horse1.jump + horse2.jump + random.uniform(1.5, 5.5)) / 3          # not really a uniform distribution, but oh well
    offspringHealth = (horse1.health + horse2.health + random.uniform(15, 30)) / 3
    offspring = Horse(speed=offspringSpeed, jump=offspringJump, health=offspringHealth)
    while offspring.speed < speed:
        if horse1 < horse2:
            if horse1 < offspring:
                horse1 = offspring
        else:
            if horse2 < offspring:
                horse2 = offspring

        offspringSpeed = (horse1.speed + horse2.speed + random.uniform(4.86, 14.57)) / 3
        offspringJump = (horse1.jump + horse2.jump + random.uniform(1.5, 5.5)) / 3          # not really a uniform distribution, but oh well
        offspringHealth = (horse1.health + horse2.health + random.uniform(15, 30)) / 3
        offspring = Horse(speed=offspringSpeed, jump=offspringJump, health=offspringHealth)

        attempts += 1

    return attempts , offspring



if __name__ == '__main__':
    horse1 = Horse(speed=11.50,jump=3.5,health=18)
    horse2 = Horse(speed=12.14,jump=2,health=26)
    average = 0
    horse = None
    for _ in range(500):
        output = breedAttemptsSpeed(horse1,horse2,speed=14.5)
        average += output[0]/500
        horse = output[1]
    print(average, horse)