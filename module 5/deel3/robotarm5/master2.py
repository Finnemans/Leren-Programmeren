from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.master import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)

# your code starts here:
kleuren = {}
index = {}

 
for i in range(3):
    robotArm.moveRight()


for _ in range(6):
    robotArm.moveRight()
    robotArm.grab()
    kleur = robotArm.scan()
    pos = robotArm.stackIndex()


    if kleur not in kleuren:
        kleuren[kleur] = 0
        index[kleur] = []
    kleuren[kleur] += 1
    index[kleur].append(pos)

    robotArm.drop()

print("Kleuren:", kleuren)
print("Indexen:", index)

#pakt 2e aantal rood, 10 dan pakt ie de 10
def aantal(kleur_item):
    return kleur_item[1]

volgorde = sorted(kleuren.items(), key=aantal, reverse=True)
print("Volgorde:", volgorde)

doelIndex = 0
for kleur, aantal in volgorde:
    for pos in index[kleur]:

        huidig = robotArm.stackIndex()
        while huidig < pos:
            robotArm.moveRight()
            huidig += 1
        while huidig > pos:
            robotArm.moveLeft()
            huidig -= 1

        robotArm.grab()
        while huidig > doelIndex:
            robotArm.moveLeft()
            huidig -= 1
        while huidig < doelIndex:
            robotArm.moveRight()
            huidig += 1
        robotArm.drop()
    doelIndex += 1

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

