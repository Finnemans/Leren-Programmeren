from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.master import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here:
kleuren = []

def verplaatsNaar(x):
    huidig = robotArm.stackIndex()
    while huidig < x:
        robotArm.moveRight()
        huidig += 1
    while huidig > x:
        robotArm.moveLeft()
        huidig -= 1

for x in range(10):
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur not in kleuren:
        kleuren.append(kleur)
        robotArm.drop()
        robotArm.moveRight()
    else:
        doelIndex = kleuren.index(kleur)
        verplaatsNaar(doelIndex)
        robotArm.drop()
        break

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

