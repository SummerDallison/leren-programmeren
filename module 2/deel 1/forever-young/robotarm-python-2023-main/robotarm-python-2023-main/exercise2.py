from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()

for i in range(9):
    robotArm.moveRight()

robotArm.drop()

for i in range(5):
    robotArm.moveLeft()

robotArm.grab()

for i in range(5):
    robotArm.moveRight()

robotArm.drop()

robotArm.moveLeft()
robotArm.moveLeft()

robotArm.grab()

robotArm.moveRight()
robotArm.moveRight()

robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()