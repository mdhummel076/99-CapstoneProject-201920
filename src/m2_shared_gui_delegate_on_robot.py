"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and James Werne, Matt Hummel, Luke Spannan.
  Winter term, 2018-2019.
"""

import rosebot
import time



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

    def robot_proximity_tone(self, frequency, inc_frequency):

        print('Start at', int(frequency), 'Hz, then increase by', int(inc_frequency), 'Hz per inch')
        x0 = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        self.robot.sound_system.tone_maker.play_tone(int(frequency), 500)

        if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() > 2:
            self.robot.drive_system.go(75, 75)

        while self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() > 2:
            x = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            self.robot.sound_system.tone_maker.play_tone((x0 - x)*int(inc_frequency) + int(frequency), 500)

        self.robot.drive_system.stop()
        self.robot.arm_and_claw.calibrate_arm()

    def robot_point_to_object(self):

        x = self.robot.sensor_system.camera.get_biggest_blob().center.x
        while x > 125:
            self.robot.drive_system.spin_clockwise_until_sees_object(22, 200)
            x = self.robot.sensor_system.camera.get_biggest_blob().center.x
            time.sleep(0.01)

        while x < 115:
            self.robot.drive_system.spin_counterclockwise_until_sees_object(22, 200)
            x = self.robot.sensor_system.camera.get_biggest_blob().center.x
            time.sleep(0.01)

    def go_forward_until_distance_is_less_than(self, inches, speed):
        self.robot.drive_system.go_forward_until_distance_is_less_than(int(inches),int(speed))

    def go_backward_until_distance_is_greater_than(self, inches, speed):
        self.robot.drive_system.go_backward_until_distance_is_greater_than(int(inches),int(speed))

    def go_until_distance_is_within(self, delta_inches, speed):
        self.robot.drive_system.go_until_distance_is_within(int(delta_inches),int(speed))

    def robot_proximity_led(self, frequency, inc_frequency):
        x = 1
        self.robot.drive_system.left_motor.turn_on(50)
        self.robot.drive_system.right_motor.turn_on(50)
        y = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        while y>2:
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 5:
                x = x +inc_frequency
            self.robot.led_system.left_led.turn_on()
            self.robot.led_system.right_led.turn_off()
            time.sleep(1/(int(frequency)+int(x)))
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 5:
                x = x + inc_frequency
            self.robot.led_system.left_led.turn_off()
            self.robot.led_system.right_led.turn_on()
            time.sleep(1/(int(frequency)+int(x)))
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 5:
                x = x + inc_frequency
            self.robot.led_system.left_led.turn_on()
            self.robot.led_system.right_led.turn_on()
            time.sleep(1/(int(frequency)+int(x)))
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 5:
                x = x + inc_frequency
            self.robot.led_system.left_led.turn_off()
            self.robot.led_system.right_led.turn_off()
            time.sleep(1/(int(frequency)+int(x)))
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 5:
                x = x + inc_frequency
            y = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        self.robot.drive_system.stop()
        self.robot.arm_and_claw.calibrate_arm()

    def camera_proximity_led(self):
        x = self.robot.sensor_system.camera.get_biggest_blob().center.x
        print('Outside if')
        if (x < 125):
            print('Second if')
            if (x > 115):
                print('inside if')
                self.robot_proximity_led(2,5)

    def enter_stage(self, color):
        """ Handles the enter stage function
        Makes robot drive onto poster, then drive
        until its color sensor reads yellow,
        then turns 90 degrees left and faces
        the "audience"
        :param color:
        :return:
        """
        self.robot.drive_system.go_straight_until_color_is(int(color), 50)
        t = time.time()
        self.robot.drive_system.left_motor.turn_on(-35)
        self.robot.drive_system.left_motor.turn_on(35)
        while time.time() - t < 2.5:
            time.time()
        self.robot.drive_system.left_motor.turn_off()
        self.robot.drive_system.right_motor.turn_off()

        return

    def exit_stage(self):
        """ Handles the exit stage feature
        Makes robot turn 90 degrees left,
        then drive off stage (until robot is off
        poster)
        :return:
        """
        self.robot.drive_system.left_motor.turn_on(-35)
        self.robot.drive_system.right_motor.turn_on(35)
        t = time.time()
        while time.time() - t < 2.5:
            time.time()
        self.robot.drive_system.left_motor.turn_off()
        self.robot.drive_system.right_motor.turn_off()

        dark = 5
        self.robot.drive_system.go_straight_until_intensity_is_less_than(dark, 50)
        self.robot.drive_system.go(50, 50)
        time.sleep(2)
        self.robot.drive_system.stop()

        return

    def apology(self):
        phrase = "Uhh, I think I left my stove running"
        self.robot.sound_system.speech_maker.speak(phrase).wait()
        time.sleep(1)
        phrase1 = "My house has probably burned down by now"
        self.robot.sound_system.speech_maker.speak(phrase1).wait()
        time.sleep(1)
        phrase2 = "I best move along, uhh bye"
        self.robot.sound_system.speech_maker.speak(phrase2).wait()
        time.sleep(1)

    def introduction(self):

        phrase = 'Hi everyone, hope you all are doing well.'
        self.robot.sound_system.speech_maker.speak(phrase).wait()
        time.sleep(1)
        phrase2 = "I'd like to perform a song for you now. Hope you enjoy."
        self.robot.sound_system.speech_maker.speak(phrase2).wait()
        time.sleep(1)

    def verse(self):

        phrase1 = 'Some things in life are bad.'
        self.robot.sound_system.speech_maker.speak(phrase1).wait()
        time.sleep(0.5)
        phrase2 = 'They can really make you mad.'
        self.robot.sound_system.speech_maker.speak(phrase2).wait()
        time.sleep(0.5)
        phrase3 = 'Other things just make you swear and curse.'
        self.robot.sound_system.speech_maker.speak(phrase3).wait()
        time.sleep(0.5)
        phrase4 = "When you're chewing life's gristle."
        self.robot.sound_system.speech_maker.speak(phrase4).wait()
        time.sleep(0.5)
        phrase5 = "Don't grumble, give a whistle."
        self.robot.sound_system.speech_maker.speak(phrase5).wait()
        time.sleep(0.5)
        phrase6 = "And this'll help things turn out for the best"
        self.robot.sound_system.speech_maker.speak(phrase6).wait()
        time.sleep(0.5)

    def chorus(self):
        phrase1 = "Aaaaaaand."
        self.robot.sound_system.speech_maker.speak(phrase1).wait()
        time.sleep(0.5)
        phrase2 = 'Always, look on, the bright, side, of life'
        self.robot.sound_system.speech_maker.speak(phrase2).wait()
        time.sleep(0.5)

        whistle1 = [(784, 185, 2.5), (660, 185, 377.5), (494, 185, 2.5), (440, 185, 190), (494, 185, 2.5),
                    (523, 185, 190), (660, 185, 2.5), (587, 185, 190)]
        self.robot.sound_system.tone_maker.play_tone_sequence(whistle1).wait()

        phrase3 = 'Always, look on, the light, side, of life'
        self.robot.sound_system.speech_maker.speak(phrase3).wait()
        self.robot.sound_system.tone_maker.play_tone_sequence(whistle1).wait()
        time.sleep(5)
        phrase4 = "Thank you for listening to me perform. Good night!"
        self.robot.sound_system.speech_maker.speak(phrase4).wait()

    def encore(self):
        phrase1 = "I have one more song for you all."
        self.robot.sound_system.speech_maker.speak(phrase1).wait()
        time.sleep(3)

        notes = [(294, 120, 5), (294, 120, 5), (587, 120, 130), (440, 120, 255), (415, 120, 5), (392, 120, 5),
                 (349, 245, 5), (294, 120, 5), (349, 120, 5), (392, 120, 5)]

        for k in range(4):
            self.robot.sound_system.tone_maker.play_tone_sequence(notes).wait()

    def check_anxiety(self, mqtt_sender, dis, window):
        dis[0] = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        mqtt_sender.send_message('return anxiety', [dis, window])

    def get_distance_in_inches(self):
        self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()









