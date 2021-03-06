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
    """ Initializes robot delegate object for
    computer to communicate with robot """

    def __init__(self, robot):

        self.robot = robot
        self.enabled = True

    def print(self, message):
        print(message)

    # ---------- Sprint 3 ---------- #

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
        self.robot.drive_system.left_motor.turn_on(35)
        while time.time() - t < 4:
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
        self.robot.drive_system.left_motor.turn_on(35)
        t = time.time()
        while time.time() - t < 4:
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
        """ Handles apology to audience.
        Robot uses speech maker to say a
        predetermined set of phrases """

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
        """ Handles introduction to audience.
        Robot uses speech maker to say
        predetermined set of phrases """

        phrase = 'Hi everyone, hope you all are doing well.'
        self.robot.sound_system.speech_maker.speak(phrase).wait()
        time.sleep(5)
        phrase2 = "I'd like to perform a song for you now. Hope you enjoy."
        self.robot.sound_system.speech_maker.speak(phrase2).wait()
        time.sleep(5)

    def verse(self):
        """ Handles verse. Robot uses speech maker
        to *sing* lyrics to 'Always Look on the Bright
        Side of Life' from Monty Python's Life of Brian."""

        phrase1 = 'Some things in life are bad.'
        self.robot.sound_system.speech_maker.speak(phrase1).wait()
        time.sleep(1)
        phrase2 = 'They can really make you mad.'
        self.robot.sound_system.speech_maker.speak(phrase2).wait()
        time.sleep(1)
        phrase3 = 'Other things just make you swear and curse.'
        self.robot.sound_system.speech_maker.speak(phrase3).wait()
        time.sleep(1)
        phrase4 = "When you're chewing life's gristle."
        self.robot.sound_system.speech_maker.speak(phrase4).wait()
        time.sleep(1)
        phrase5 = "Don't grumble, give a whistle."
        self.robot.sound_system.speech_maker.speak(phrase5).wait()
        time.sleep(1)
        phrase6 = "And this'll help things turn out for the best"
        self.robot.sound_system.speech_maker.speak(phrase6).wait()
        time.sleep(1)

    def chorus(self):
        """ Handles chorus. Robot uses speech maker
        & tone generator to perform chorus of 'Always Look
        on the Bright Side of Life', then bids goodnight
        to audience """

        phrase1 = "Aaaaaaand."
        self.robot.sound_system.speech_maker.speak(phrase1).wait()
        time.sleep(1)
        phrase2 = 'Always, look on, the bright, side, of life'
        self.robot.sound_system.speech_maker.speak(phrase2).wait()
        time.sleep(2)

        whistle1 = [(784, 185, 2.5), (660, 185, 377.5), (494, 185, 2.5), (440, 185, 190), (494, 185, 2.5),
                    (523, 185, 190), (660, 185, 2.5), (587, 185, 190)]
        time.sleep(1)
        self.robot.sound_system.tone_maker.play_tone_sequence(whistle1).wait()

        phrase3 = 'Always, look on, the light, side, of life'
        self.robot.sound_system.speech_maker.speak(phrase3).wait()
        time.sleep(2)
        self.robot.sound_system.tone_maker.play_tone_sequence(whistle1).wait()
        time.sleep(4)
        phrase4 = "Thank you for listening to me perform. Good night!"
        self.robot.sound_system.speech_maker.speak(phrase4).wait()

    def encore(self):
        """ Handles encore. Uses robot's speechmaker
        and tone generator to address audience one last time
        and to perform one final song """

        phrase1 = "I have one more song for you all."
        self.robot.sound_system.speech_maker.speak(phrase1).wait()
        time.sleep(3)

        notes = [(294, 120, 5), (294, 120, 5), (587, 120, 130), (440, 120, 255), (415, 120, 130), (392, 120, 130),
                 (349, 245, 5), (294, 120, 5), (349, 120, 5), (392, 120, 5), (294, 120, 5), (294, 120, 5),
                 (587, 120, 130), (440, 120, 255), (415, 120, 130), (392, 120, 130), (349, 245, 5), (294, 120, 5),
                 (349, 120, 5), (392, 120, 5), (294, 120, 5), (294, 120, 5), (587, 120, 130), (440, 120, 255),
                 (415, 120, 130), (392, 120, 130), (349, 245, 5), (294, 120, 5), (349, 120, 5), (392, 120, 5),
                 (294, 120, 5), (294, 120, 5), (587, 120, 130), (440, 120, 255), (415, 120, 130), (392, 120, 130),
                 (349, 245, 5), (294, 120, 5), (349, 120, 5), (392, 120, 5)]

        self.robot.sound_system.tone_maker.play_tone_sequence(notes).wait()
        time.sleep(4)

        phrase2 = "Thank you, goodnight!"
        self.robot.sound_system.speech_maker.speak(phrase2).wait()
        time.sleep(3)

    def get_distance_in_inches(self):
        """ Calls get_distance_in_inches method on robot """
        self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()

    def get_touch_press(self):
        """ Calls is_pressed method for touch sensor on robot"""
        self.robot.sensor_system.touch_sensor.is_pressed()

    # ------- Sprints 1-2 -------- #

    def go(self, lval, rval):
        chassis = self.robot.drive_system
        chassis.go(int(lval), int(rval))
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

    def move_arm_to_position(self, position):
        arm = self.robot.arm_and_claw
        arm.move_arm_to_position(int(position))

    def go_straight_for_seconds(self, seconds, speed):
        chassis = self.robot.drive_system
        chassis.go_straight_for_seconds(int(seconds), int(speed))

    def go_straight_for_inches_using_time(self, inches, speed):
        chassis = self.robot.drive_system
        chassis.go_straight_for_inches_using_time(int(inches), int(speed))

    def go_straight_for_inches_using_encoder(self, inches, speed):
        chassis = self.robot.drive_system
        chassis.go_straight_for_inches_using_encoder(int(inches), int(speed))

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

    def CW(self, speed, area):

        self.robot.drive_system.spin_clockwise_until_sees_object(int(speed), int(area))

    def CCW(self, speed, area):

        self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), int(area))

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
            self.robot.sound_system.tone_maker.play_tone((x0 - x) * int(inc_frequency) + int(frequency), 500)

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
        self.robot.drive_system.go_forward_until_distance_is_less_than(int(inches), int(speed))

    def go_backward_until_distance_is_greater_than(self, inches, speed):
        self.robot.drive_system.go_backward_until_distance_is_greater_than(int(inches), int(speed))

    def go_until_distance_is_within(self, delta_inches, speed):
        self.robot.drive_system.go_until_distance_is_within(int(delta_inches), int(speed))

    def robot_proximity_led(self, frequency, inc_frequency):
        x = 1
        self.robot.drive_system.left_motor.turn_on(50)
        self.robot.drive_system.right_motor.turn_on(50)
        y = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        while y > 2:
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 5:
                x = x + inc_frequency
            self.robot.led_system.left_led.turn_on()
            self.robot.led_system.right_led.turn_off()
            time.sleep(1 / (int(frequency) + int(x)))
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 5:
                x = x + inc_frequency
            self.robot.led_system.left_led.turn_off()
            self.robot.led_system.right_led.turn_on()
            time.sleep(1 / (int(frequency) + int(x)))
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 5:
                x = x + inc_frequency
            self.robot.led_system.left_led.turn_on()
            self.robot.led_system.right_led.turn_on()
            time.sleep(1 / (int(frequency) + int(x)))
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 5:
                x = x + inc_frequency
            self.robot.led_system.left_led.turn_off()
            self.robot.led_system.right_led.turn_off()
            time.sleep(1 / (int(frequency) + int(x)))
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
                self.robot_proximity_led(2, 5)
