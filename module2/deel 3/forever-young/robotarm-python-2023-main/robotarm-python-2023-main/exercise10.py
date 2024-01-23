from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
aantal = 9
for x in range(5):
    robotArm.grab()
    
    for i in range(aantal):
        robotArm.moveRight()
    aantal -= 1
    robotArm.drop()

    for i in range(aantal):
        robotArm.moveLeft()
    aantal -= 1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()