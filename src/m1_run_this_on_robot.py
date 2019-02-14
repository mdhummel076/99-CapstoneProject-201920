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
    delegate = Delegate(robot)
    client = com.MqttClient(delegate)
    client.connect_to_pc()

    while True:
        if not delegate.enabled:
            break
        time.sleep(0.01)

class Delegate(shared_gui_delegate_on_robot.Delegate):

    def m1BeepDrive(self,initRate,rate):
        startDistance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        beepCo = (1/int(initRate))/startDistance
        self.robot.drive_system.go(50,50)
        while True:
            distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            if distance < 2:
                break
            self.beep(1)
            time.sleep(max((1/int(initRate))-(startDistance-distance)*(1/int(rate)),0))
        self.stop()
        self.calibrate_arm()

    def centerOnTarget(self):
        while True:
            error = self.robot.sensor_system.camera.get_biggest_blob().center.x-140
            if ((error <= 10) & (error >= -10)) | (error == -140):
                break
            if error > 10:
                self.go(30, -30)
            if error < -10:
                self.go(-30, 30)
        self.stop()

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()