"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Matt Hummel.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui
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

    client = com.MqttClient()
    client.connect_to_ev3()
    time.sleep(1)

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------

    root = tkinter.Tk()
    root.title("EV3 Remote")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------

    mainFrame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    mainFrame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------

    teleopFrame, armFrame, controlFrame, driveSystemFrame = get_shared_frames(mainFrame,client)


    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------

    teleopFrame.grid(row = 0, column = 0)
    armFrame.grid(row = 1, column = 0)
    controlFrame.grid(row = 3, column = 0)
    driveSystemFrame.grid(row = 4,column = 0)


    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------

    root.mainloop()

def get_shared_frames(main_frame, mqtt_sender):
    teleopFrame = shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    armFrame = shared_gui.get_arm_frame(main_frame,mqtt_sender)
    controlFrame = shared_gui.get_control_frame(main_frame,mqtt_sender)
    driveSystemFrame = shared_gui.get_drivesystem_frame(main_frame,mqtt_sender)

    return teleopFrame, armFrame, controlFrame, driveSystemFrame


def grid_frames(teleop_frame, arm_frame, control_frame):
    pass


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
