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
import m1_run_this_on_robot


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicate via MQTT with the GUI code that runs on the LAPTOP.
    """
    print('Text2')
    real_deal()
    grab_yellow_object()

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
def grab_yellow_object():
    robot = rosebot.RoseBot()
    delegate = shared_gui_delegate_on_robot.Delegate(robot)
    robot.sensor_system.camera.set_signature("SIG1")
    b1 = robot.sensor_system.camera.get_biggest_blob()
    # robot.drive_system.spin_counterclockwise_until_sees_object(50,100)
    # while robot.drive_system.spin_counterclockwise_until_sees_object(50,100):
    #             robot.drive_system.go_forward_until_distance_is_less_than(1,50)
    #             if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()<10:
    #                 robot.sound_system.speech_maker.speak("I am 10 inches away from target")
    #             if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()<5:
    #                 robot.sound_system.speech_maker.speak("I am 5 inches away from target")
    #             if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()<1:
    #                 robot.sound_system.speech_maker.speak("I now have the target")
    #                 robot.arm_and_claw.raise_arm()
    #                 robot.drive_system.go(-50,-50)
    #                 if robot.sensor_system.color_sensor.get_color() == 6:
    #                     robot.arm_and_claw.lower_arm()
    print('Text')

def sprint_3():
    robot = rosebot.RoseBot()
main()