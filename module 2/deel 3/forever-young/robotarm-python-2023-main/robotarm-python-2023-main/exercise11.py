from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
for i in range(8):
    robotArm.moveRight()

for i in range(9):
    robotArm.grab()
    color = robotArm.scan()
    print(robotArm.scan())
    if color == "white":
        robotArm.moveRight()
        robotArm.drop()
        if i < 8:
            robotArm.moveLeft()
            robotArm.moveLeft()

    else:
        robotArm.drop()
        if i < 8:
            robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()