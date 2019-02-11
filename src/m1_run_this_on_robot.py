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
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.\

      combination: 18-28-10
    """

    operate()



def operate():

    robot = rosebot.RoseBot()
    Delegate = shared_gui_delegate_on_robot.Delegate(robot)
    client = com.MqttClient(Delegate)
    client.connect_to_pc()

    while True:
        if not Delegate.enabled:
            break
        time.sleep(0.01)
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------

main()