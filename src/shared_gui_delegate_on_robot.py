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
        self.enabled = True

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

    def beep(self, n):
        for k in range(int(n)):
            beeper = self.robot.sound_system.beeper
            beeper.beep().wait()

    def tone(self, frequency, duration):
        sounds = self.robot.sound_system.tone_maker
        sounds.play_tone(int(frequency), int(duration))

    def speak(self, phrase):
        sounds = self.robot.sound_system.speech_maker
        sounds.speak(phrase)

    def quit(self):
        self.enabled = False

    def printData(self):

        self.robot.drive_system.display_camera_data()

    def CW(self,speed,area):

        self.robot.drive_system.spin_clockwise_until_sees_object(int(speed),int(area))

    def CCW(self,speed,area):

        self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed),int(area))

    def go_straight_until_intensity_is_less_than(self, intensity, speed):

        self.robot.drive_system.go_straight_until_intensity_is_less_than(int(intensity), int(speed))

    def go_straight_until_intensity_is_greater_than(self, intensity, speed):
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(int(intensity), int(speed))

    def go_straight_until_color_is(self, color, speed):
        self.robot.drive_system.go_straight_until_color_is(int(color), int(speed))

    def go_straight_until_color_is_not(self, color, speed):
        self.robot.drive_system.go_straight_until_color_is_not(int(color), int(speed))

    def m1BeepDrive(self,initRate,rate):
        startDistance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        beepCo = (1/int(initRate))/startDistance
        self.robot.drive_system.go(50,50)
        while True:
            distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            if distance < 2:
                break
            self.beep(1)
            time.sleep(beepCo*(distance)+(distance-startDistance)*(1/int(rate)))
        self.stop()


    def go_forward_until_distance_is_less_than(self, inches, speed):
        self.robot.drive_system.go_forward_until_distance_is_less_than(int(inches),int(speed))

    def go_backward_until_distance_is_greater_than(self, inches, speed):
        self.robot.drive_system.go_backward_until_distance_is_greater_than(int(inches),int(speed))

    def go_until_distance_is_within(self, delta_inches, speed):
        self.robot.drive_system.go_until_distance_is_within(int(delta_inches),int(speed))