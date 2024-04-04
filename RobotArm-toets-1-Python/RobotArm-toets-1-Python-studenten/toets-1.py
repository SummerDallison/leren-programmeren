from RobotArm import RobotArm

robotArm = RobotArm('toets-1')

# Jouw python instructies zet je vanaf hier:

for i in range(3):
    if i == 0:
        for i in range(4):
            robotArm.moveRight()
    else:
        for i in range(3):
            robotArm.moveRight()
    robotArm.grab()
    for i in range(3):
        robotArm.moveLeft()
    robotArm.drop()

for i in range(3):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()

for i in range(4):
    robotArm.moveRight()
robotArm.grab()
for i in range(3):
    robotArm.moveRight()
robotArm.drop()

for i in range(2):
    for i in range(3):
        robotArm.moveLeft()
    robotArm.grab()
    for i in range(3):
        robotArm.moveRight()
    robotArm.drop()

for i in range(3):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()