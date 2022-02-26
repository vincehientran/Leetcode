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

        offspringSpeed = (horse1.speed + horse2.speed + random.uniform(4.86, 14.23)) / 3
        offspringJump = (horse1.jump + horse2.jump + random.uniform(1.5, 5.5)) / 3          # not really a uniform distribution, but oh well
        offspringHealth = (horse1.health + horse2.health + random.uniform(15, 30)) / 3
        offspring = Horse(speed=offspringSpeed, jump=offspringJump, health=offspringHealth)

        attempts += 1

    return attempts , offspring

def stats(data):
    data = data.split()

    speedIdx = 0
    while data[speedIdx] != '"minecraft:generic.movement_speed"},':
        speedIdx += 1
    speedIdx -= 2

    healthIdx = speedIdx
    while data[healthIdx] != '"minecraft:generic.max_health"},':
        healthIdx += 1
    healthIdx -= 2

    jumpIdx = healthIdx
    while data[jumpIdx] != '"minecraft:horse.jump_strength"}],':
        jumpIdx += 1
    jumpIdx -= 2
    
    return float(data[speedIdx][:-2])*42.163, int(float(data[healthIdx][:-2])//2), (float(data[jumpIdx][:-2])**1.7) * 5.293
    
def printStats(stats):
    print('\nspeed:\t',stats[0],'b/s')
    print('health:\t',stats[1],'h')
    print('jump:\t',stats[2],'b\n')


if __name__ == '__main__':
    data = '/summon minecraft:horse -738.30 71.00 193.50 {Brain: {memories: {}}, HurtByTimestamp: 0, Tame: 0b, Attributes: [{Base: 0.2721256386962286d, Name: "minecraft:generic.movement_speed"}, {Base: 22.113024776033466d, Name: "minecraft:generic.max_health"}, {Base: 0.0d, Name: "minecraft:generic.armor"}, {Base: 0.698697627513987d, Name: "minecraft:horse.jump_strength"}], Invulnerable: 0b, FallFlying: 0b, ForcedAge: 0, PortalCooldown: 0, AbsorptionAmount: 0.0f, Bred: 0b, FallDistance: 0.0f, InLove: 0, EatingHaystack: 0b, DeathTime: 0s, HandDropChances: [0.085f, 0.085f], PersistenceRequired: 0b, Age: -23910, Motion: [0.0d, -0.0784000015258789d, 0.0d], Health: 53.0f, LeftHanded: 0b, Air: 300s, OnGround: 1b, Rotation: [89.7469f, -31.304f], HandItems: [{}, {}], Variant: 2, ArmorDropChances: [0.085f, 0.085f, 0.0f, 0.085f], Fire: -1s, ArmorItems: [{}, {}, {}, {}], Temper: 0, CanPickUpLoot: 0b, HurtTime: 0s}'
    printStats(stats(data))
    horse1 = Horse(speed=12.56,jump=3.5,health=18)
    horse2 = Horse(speed=12.40,jump=2,health=26)
    average = 0
    horse = None
    for _ in range(500):
        output = breedAttemptsSpeed(horse1,horse2,speed=13)
        average += output[0]/500
        horse = output[1]
    print(average, horse)