#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

robot.straight(575)
ev3.speaker.beep()


robot.turn(90)
ev3.speaker.beep()

# 650 -> 630
# 630 -> 640
robot.straight(640)
ev3.speaker.beep()


robot.turn(90)
ev3.speaker.beep()

# 600 -> 575
# 575 -> 550
robot.straight(550)
ev3.speaker.beep()


robot.turn(90)
ev3.speaker.beep()


robot.straight(645)