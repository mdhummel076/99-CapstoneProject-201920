# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.


import ev3dev.ev3 as ev3
import time
import math

def go_straight_until_intensity_is_less_than(self, intensity, speed):
    """
    Goes straight at the given speed until the intensity returned
    by the color_sensor is less than the given intensity.
    """

    self.color_sensor = sensor_system.color_sensor # goes in __init__ for Drivesystem
    print(self.color_sensor.reflected_light_intensity)
    self.left_motor.turn_on(speed)
    self.right_motor.turn_on(speed)

    while self.color_sensor.reflected_light_intensity >= intensity:
        time.sleep(0.01)

    self.left_motor.turn_off()
    self.right_motor.turn_off()


def go_straight_until_intensity_is_greater_than(self, intensity, speed):
    """
    Goes straight at the given speed until the intensity returned
    by the color_sensor is greater than the given intensity.
    """

    print(self.color_sensor.reflected_light_intensity)
    self.left_motor.turn_on(speed)
    self.right_motor.turn_on(speed)

    while self.color_sensor.reflected_light_intensity <= intensity:
        time.sleep(0.01)

    self.left_motor.turn_off()
    self.right_motor.turn_off()


def go_straight_until_color_is(self, color, speed):
    """
    Goes straight at the given speed until the color returned
    by the color_sensor is equal to the given color.

    Colors can be integers from 0 to 7 or any of the strings
    listed in the ColorSensor class.

    If the color is an integer (int), then use the  get_color   method
    to access the color sensor's color.  If the color is a string (str),
    then use the   get_color_as_name   method to access
    the color sensor's color.
    """

    print(self.color_sensor.color)
    self.left_motor.turn_on(speed)
    self.right_motor.turn_on(speed)

    while self.color_sensor.color != color:
        time.sleep(0.01)

    self.left_motor.turn_off()
    self.right_motor.turn_off()


def go_straight_until_color_is_not(self, color, speed):
    """
    Goes straight at the given speed until the color returned
    by the color_sensor is NOT equal to the given color.

    Colors can be integers from 0 to 7 or any of the strings
    listed in the ColorSensor class.
    """

    print(self.color_sensor.color)
    self.left_motor.turn_on(speed)
    self.right_motor.turn_on(speed)

    while self.color_sensor.color == color:
        time.sleep(0.01)

    self.left_motor.turn_off()
    self.right_motor.turn_off()