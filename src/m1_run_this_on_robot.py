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

    #Sets up a robot instance, robot delegate, and mqtt client
    robot = rosebot.RoseBot()
    delegate = Delegate(robot)
    client = com.MqttClient(delegate)
    client.connect_to_pc()
    delegate.client = client
    while True:
        if not delegate.enabled:
            break
        time.sleep(0.01)

    #Creates the delegate to handle laptop commands. Each method is a simon says action that implements the RoseBot class
class Delegate(shared_gui_delegate_on_robot.Delegate):

    def __init__(self, robot):

        self.client = None
        self.robot = robot
        self.enabled = True

    def Move(self):
        self.go_straight_for_seconds(1.5,50)
        self.go_straight_for_seconds(1.5,-50)

    def Dance(self):
        self.robot.drive_system.go(100,-100)
        time.sleep(2.5)
        self.robot.drive_system.go(-100,100)
        time.sleep(2.5)
        self.robot.drive_system.stop()

    def Stretch(self):
        self.robot.arm_and_claw.calibrate_arm()

    def Clap(self):
        self.robot.arm_and_claw.move_arm_to_position(2500)
        self.robot.arm_and_claw.lower_arm()

    def Color(self):
        color = self.robot.sensor_system.color_sensor.get_color()
        if color == 1:
            message = 'Black'
        elif color == 2:
            message = 'Blue'
        elif color == 3:
            message = 'Green'
        elif color == 4:
            message = 'Yellow'
        elif color == 5:
            message = 'Red'
        elif color == 6:
            message = 'White'
        elif color == 7:
            message = 'Brown'
        else:
            message = 'Unknown Color'

        self.client.send_message('writeText',[message])

    def Find(self):
        self.robot.drive_system.spin_counterclockwise_until_sees_object(30, 50)
        message = 'Found: ('+str(self.robot.sensor_system.camera.get_biggest_blob().center.x)+', '+str(self.robot.sensor_system.camera.get_biggest_blob().center.y)+')'
        print(message)
        self.client.send_message('writeText',[message])

    def Beep(self):
        self.beep(3)

    def Sing(self):
        self.speak('here comes, the, sun, do do do do, here comes, the, sun')


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()