from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
for i in range(8):
    robotArm.moveRight()

for i in range(9):
    robotArm.grab()
    color = robotArm.scan()
    print(robotArm.scan())
    if color == "red":
        for x in range(1 + i):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(2 + i):
            if i < 8:
                robotArm.moveLeft()
    else:
        robotArm.drop()
        if i < 8:
            robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()