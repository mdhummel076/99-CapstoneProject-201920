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
    while True:
        time.sleep(0.01)
        if delegate.enabled == False:
            break
def flight():
    #What I had done here was make a robot, that, when provoked, would go and run from the person who had touched the button.
    #However, if teh robot had gone and saw that there was an object in its way, it would go and have a "breakdown" where it spins
    #rapidly, but would shut down due to too much stress.
    Mqtt=com.MqttClient()
    robot = rosebot.RoseBot()
    button = robot.sensor_system.touch_sensor
    speech = robot.sound_system.speech_maker
    counter = 0
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0
    while True:
        if button.is_pressed() == True:
            counter = counter +1
        if counter == 1:
            counter_1=counter_1+1
            if counter_1 == 1:
                speech.speak("Hey! You poked me!")
        if counter == 2:
            counter_2 = counter_2 + 1
            if counter_2 == 1:
                speech.speak("Stop touching me!")
        if counter == 3:
            counter_3 = counter_3 + 1
            if counter_3 == 1:
                speech.speak("I can't take this! I'm going home!")
            break
        time.sleep(1)
    robot.drive_system.go(50,50)
    while True:
        x = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        print(x)
        if x<5:
            robot.drive_system.stop()
            speech.speak("Why can't I go home? I wanna go home!").wait()
            robot.drive_system.go(100,-100)
            time.sleep(5)
            speech.speak("WARNING: STRESS SENSORS OVERLOADED. SHUTDOWN IMMINENT")
            robot.drive_system.stop()
            break
        y = robot.sensor_system.color_sensor.get_color()
        if y == 6:
            robot.drive_system.stop()
            print("I made it home")
            speech.speak("I am finally home. I can now rest")
            break
        time.sleep(.1)

        time.sleep(1)
    Mqtt.send_message("flight")
def fight():
    #The function here is similar to teh flight response where it requires you to touch the sensor for it to begin, but
    #instead of running away from yu it would actually go and try to "attack" you. For this to occur, you need to press the touch sensor
    #three times.
    Mqtt = com.MqttClient()
    robot = rosebot.RoseBot()
    button = robot.sensor_system.touch_sensor
    speech = robot.sound_system.speech_maker
    counter = 0
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0
    while True:
        if button.is_pressed() == True:
            counter = counter +1
        if counter == 1:
            counter_1 = counter_1 + 1
            if counter_1 == 1:
                speech.speak("Hey! Watch what you're doing, twerp!")
        if counter == 2:
            counter_2 = counter_2 + 1
            if counter_2 == 1:
                speech.speak("You'll be gettin a knuckle sandwich, punk!")
        if counter == 3:
            counter_3 = counter_3 + 1
            if counter_3 == 1:
                speech.speak("Alright bub, you asked for it!")
                break
    robot.drive_system.go(50,-50)
    time.sleep(2.8)
    robot.drive_system.go_forward_until_distance_is_less_than(2,50)
    speech.speak("Take this, you cur!")
    robot.arm_and_claw.raise_arm()
    time.sleep(1)
    speech.speak("Get ready for the Grand Hand Slam!")
    time.sleep(3)
    robot.arm_and_claw.lower_arm()
    speech.speak("Serves you right, you jerk!")
    Mqtt.send_message("fight")




def sprint_3():
    robot = rosebot.RoseBot()
main()