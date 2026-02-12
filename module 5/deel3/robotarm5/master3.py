from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.master import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[3],0)

# your code starts here:

toren1 = 0
toren2 = 1
toren3 = 8
toren4 = 9
begin = 3

def verplaatsNaar(x):
    huidig = robotArm.stackIndex()
    while huidig < x:
        robotArm.moveRight()
        huidig += 1
    while huidig > x:
        robotArm.moveLeft()
        huidig -= 1

def kleurNaarToren(kleur):
    return torens.get(kleur, -1)

kleuren = []
toren_posities = [toren1, toren2, toren3, toren4]
torens = {}

verplaatsNaar(begin)
for x in range(4):
    for _ in range(4):

        for i in range(1):
            robotArm.grab()
            kleur = robotArm.scan()

            if kleur not in torens:
                torens[kleur] = toren_posities[len(torens)]
                kleuren.append(kleur)

            startPositie = robotArm.stackIndex() 
            print(startPositie)
            doelToren = torens[kleur]


            verplaatsNaar(doelToren)
            robotArm.drop()

            if  _ < 3:
                verplaatsNaar(startPositie)
                robotArm.moveRight()
            else:
                verplaatsNaar(begin)





print(kleuren)
print(torens)

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

