"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and James Werne, Matt Hummel, Luke Spannan.
  Winter term, 2018-2019.
"""

import rosebot

class Delegate(object):

    def __init__(self, robot):

        self.robot = robot

    def print(self,message):
        print(message)

    def go(self,lval,rval):
        chassis = self.robot.drive_system
        chassis.go(int(lval),int(rval))
        print('going')

    def stop(self):
        chassis = self.robot.drive_system
        chassis.stop()

    def raise_arm(self):
        arm = self.robot.arm_and_claw
        arm.raise_arm()

    def lower_arm(self):
        arm = self.robot.arm_and_claw
        arm.lower_arm()

    def calibrate_arm(self):
        arm = self.robot.arm_and_claw
        arm.calibrate_arm()

    def move_arm_to_position(self,position):
        arm = self.robot.arm_and_claw
        arm.move_arm_to_position(int(position))

    def go_straight_for_seconds(self, seconds, speed):
        chassis = self.robot.drive_system
        chassis.go_straight_for_seconds(int(seconds),int(speed))

    def go_straight_for_inches_using_time(self, inches, speed):
        chassis = self.robot.drive_system
        chassis.go_straight_for_inches_using_time(int(inches),int(speed))

    def go_straight_for_inches_using_encoder(self, inches, speed):
        chassis = self.robot.drive_system
        chassis.go_straight_for_inches_using_encoder(int(inches),int(speed))
