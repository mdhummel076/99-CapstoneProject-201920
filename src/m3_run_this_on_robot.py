"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Luke Spannan.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicate via MQTT with the GUI code that runs on the LAPTOP.
    """
    print('Text2')
    real_deal()
    fight()

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
# def run_test_arm():
#     robot = rosebot.RoseBot()
#     robot.arm_and_claw.raise_arm()
def real_deal():
    robot = rosebot.RoseBot()
    delegate = shared_gui_delegate_on_robot.Delegate(robot)
    receiver = com.MqttClient(delegate)
    receiver.connect_to_pc()
def flight():
    robot = rosebot.RoseBot()
    button = robot.sensor_system.touch_sensor
    speech = robot.sound_system.speech_maker
    counter = 0
    while True:
        if button.is_pressed() == True:
            counter = counter +1
        if counter == 1:
            speech.speak("Hey! You poked me!")
        if counter == 2:
            speech.speak("Stop touching me!")
        if counter == 3:
            speech.speak("I can't take this! I'm going home!")
            robot.drive_system.go_straight_until_color_is(6, 50)
            if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()>3:
                speech.speak("Why can't I go home? I wanna go home!")
                robot.drive_system.go(50,-50)
                time.sleep(5)
                speech.speak("WARNING: STRESS SENSORS OVERLOADED. SHUTDOWN IMMINENT")
                robot.drive_system.stop()
                break
            speech.speak("I am home. I can now rest")
            break
        time.sleep(1)
def fight():
    robot = rosebot.RoseBot()
    button = robot.sensor_system.touch_sensor
    speech = robot.sound_system.speech_maker
    counter = 0
    while True:
        if button.is_pressed() == True:
            counter = counter +1
        if counter == 1:
            speech.speak("Hey! Watch what you're doing, twerp!")
        if counter == 2:
            speech.speak("You'll be gettin a knuckle sandwich, punk!")
        if counter == 3:
            speech.speak("Alright bub, you asked for it!")
            robot.drive_system.go(50,-50)
            time.sleep(.5)
            if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()<10:
                speech.speak("Come here, chicken!")
            robot.drive_system.go_forward_until_distance_is_less_than()
            break
        time.sleep(1)


def sprint_3():
    robot = rosebot.RoseBot()
main()