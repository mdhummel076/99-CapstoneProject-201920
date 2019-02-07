"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Matt Hummel.
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
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """

    #operate()

    robot = rosebot.RoseBot()
    robot.arm_and_claw.move_arm_to_position(4000)


def operate():

    robot = rosebot.RoseBot

    client = com.MqttClient(shared_gui_delegate_on_robot.Delegate(robot))
    client.connect_to_pc()

    while True:
        time.sleep(0.01)
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------

main()