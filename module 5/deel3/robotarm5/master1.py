from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.master import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[1],0)

# your code starts here:
eerste_kleur = None
vorige_kleur = None
andere_kleur = None

for i in range(10):
    robotArm.grab()
    kleur = robotArm.scan()
    positie = i + 1

    if eerste_kleur is None:
        eerste_kleur = kleur
        vorige_kleur = kleur

    elif i == 1:
        vorige_kleur = kleur

    elif i == 2:
        if kleur == vorige_kleur and vorige_kleur != eerste_kleur:
            andere_kleur = 1
            robotArm.drop()
            break

        elif kleur == eerste_kleur and vorige_kleur != eerste_kleur:
            andere_kleur = 2
            robotArm.drop()
            break

        elif kleur != eerste_kleur and kleur != vorige_kleur:
            andere_kleur = 3
            robotArm.drop()
            break

    else:
        if kleur != eerste_kleur:
            andere_kleur = positie
            robotArm.drop()
            break

    vorige_kleur = kleur
    robotArm.drop()
    robotArm.moveRight()

print(andere_kleur)

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

