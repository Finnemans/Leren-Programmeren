from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.master import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here:
spot1 = 6
spot2 = 7
spot3 = 8
spot4 = 9

spots = [spot1, spot2, spot3, spot4]

replica = 1
kleuren = []

def ontleden():
    for i in range(4):
        robotArm.grab()
        kleur = robotArm.scan()
        kleuren.append(kleur)
        robotArm.moveRight()
        robotArm.drop()
        if i < 3:
            robotArm.moveLeft()
        print(kleuren)
    for x in range(4):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        if x < 3:
            robotArm.moveRight()

def verplaatsNaar(x):
    huidig = robotArm.stackIndex()
    while huidig < x:
        robotArm.moveRight()
        huidig += 1
    while huidig > x:
        robotArm.moveLeft()
        huidig -= 1

ontleden()
i = 0
while i < len(spots):
    verplaatsNaar(spots[i])
    robotArm.grab()
    kleur = robotArm.scan()

    if len(kleuren) > 0 and kleur == kleuren[-1]:
        kleuren.pop()
        verplaatsNaar(replica)
        robotArm.drop()
        spots.pop(i)
        print(spots)
        i = 0
    else:
        robotArm.drop()
        i += 1
# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

