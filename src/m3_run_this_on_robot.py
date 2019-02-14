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

main()