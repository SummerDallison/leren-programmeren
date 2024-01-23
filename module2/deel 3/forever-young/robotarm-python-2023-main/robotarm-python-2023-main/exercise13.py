from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
aantal = 1

while True:
    robotArm.grab()

    color = robotArm.scan()
    print(robotArm.scan())

    if color != "":
        for i in range(aantal):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(aantal):
            robotArm.moveLeft()

        aantal += 1

    else:
        break

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()