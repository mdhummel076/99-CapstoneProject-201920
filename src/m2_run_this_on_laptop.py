"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Dr. Boutell, Dr. Mutchler (for the framework)
    and James Werne.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui
import rosebot
import time


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------

    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()


    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------

    root = tkinter.Tk()
    root.title("Capstone Project - James")


    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------

    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()


    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, drivesystem_frame, soundmaker_frame, \
        color_sensor_frame, cameraFrame = get_shared_frames(main_frame, mqtt_sender)
    sprint_2_frame = sprint_2_frames(main_frame, mqtt_sender)


    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------

    grid_frames(teleop_frame, arm_frame, control_frame, drivesystem_frame, soundmaker_frame, color_sensor_frame, cameraFrame,
                sprint_2_frame)


    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------

    root.mainloop()



def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    drivesystem_frame = shared_gui.get_drivesystem_frame(main_frame, mqtt_sender)
    soundmaker_frame = shared_gui.getSoundmakerFrame(main_frame,mqtt_sender)
    color_sensor_frame = shared_gui.get_ColorSensor_Frame(main_frame, mqtt_sender)
    cameraFrame = shared_gui.get_camera_frame(main_frame,mqtt_sender)

    return teleop_frame, arm_frame, control_frame, drivesystem_frame, soundmaker_frame, color_sensor_frame, cameraFrame


def grid_frames(teleop_frame, arm_frame, control_frame, drivesystem_frame, soundmaker_frame, color_sensor_frame,
                cameraFrame, sprint_2_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    drivesystem_frame.grid(row=0, column=1)
    soundmaker_frame.grid(row=1, column=1)
    color_sensor_frame.grid(row=2, column=1)
    cameraFrame.grid(row=3, column=0)
    sprint_2_frame.grid(row=3, column=1)


def sprint_2_frames(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Sprint 2: Feature 9 & 10")
    frame_label.grid(row=0, column=0)

    robot_point_to_object_button = ttk.Button(frame, text="Make Robot Point Straight to Object")
    robot_point_to_object_button.grid(row=4, column=0)

    robot_point_to_object_button['command']=lambda: handle_robot_point_to_object(mqtt_sender)

    return frame

def handle_robot_point_to_object(mqtt_sender):

    print('Make Robot Point to Object')
    robot = rosebot.RoseBot()
    x = robot.sensor_system.camera.get_biggest_blob().x
    while x > 125:
        mqtt_sender.send_message('CCW', [30, 200])
        x = robot.sensor_system.camera.get_biggest_blob().x
        time.sleep(0.01)

    while x < 115:
        mqtt_sender.send_message('CW', [30, 200])
        x = robot.sensor_system.camera.get_biggest_blob().x
        time.sleep(0.01)





# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()