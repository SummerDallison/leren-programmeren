from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:

while True:
    robotArm.grab()

    color = robotArm.scan()
    print(robotArm.scan())

    if color != "":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        break

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()