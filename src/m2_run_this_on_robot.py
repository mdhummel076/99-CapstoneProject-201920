"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Dr. Boutell, Dr. Mutchler (for the framework)
    and James Werne.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import m2_shared_gui_delegate_on_robot


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """

    real_thing()


def real_thing():
    # Connects computer to ev3 via delegate
    robot = rosebot.RoseBot()
    delegate = m2_shared_gui_delegate_on_robot.Delegate(robot)
    mqtt_receiver = com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()

    # Connects ev3 to computer via delegate
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()

    if robot.sensor_system.ir_proximity_sensor.distance_counter == 1:
        dis = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        mqtt_client.send_message('change_anxiety', [dis])
        time.sleep(1)
        robot.sensor_system.ir_proximity_sensor.distance_counter = 0

    if robot.sensor_system.touch_sensor.touch_counter == 1:
        mqtt_client.send_message('change_hostility')

    while True:
        if not delegate.enabled:
            time.sleep(0.01)



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()