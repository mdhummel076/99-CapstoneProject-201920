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

    teleopFrame, armFrame, controlFrame, driveSystemFrame, soundmakerFrame, colorFrame, cameraFrame = get_shared_frames(mainFrame,client)


    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------

    beepdriveFrame = get_beepFrame(mainFrame,client)
    simonFrame = getSimonFrame(mainFrame,client)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------

    teleopFrame.grid(row = 0, column = 0)
    armFrame.grid(row = 1, column = 0)
    controlFrame.grid(row = 2, column = 0)
    driveSystemFrame.grid(row = 3,column = 0)
    soundmakerFrame.grid(row = 4, column = 0)
    colorFrame.grid(row=0,column=1)
    cameraFrame.grid(row=1,column=1)
    beepdriveFrame.grid(row=2,column=1)
    simonFrame.grid(row=3,column=1)


    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------

    root.mainloop()

def get_shared_frames(main_frame, mqtt_sender):
    teleopFrame = shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    armFrame = shared_gui.get_arm_frame(main_frame,mqtt_sender)
    controlFrame = shared_gui.get_control_frame(main_frame,mqtt_sender)
    driveSystemFrame = shared_gui.get_drivesystem_frame(main_frame,mqtt_sender)
    soundmakerFrame = shared_gui.getSoundmakerFrame(main_frame,mqtt_sender)
    colorFrame = shared_gui.get_ColorSensor_Frame(main_frame,mqtt_sender)
    cameraFrame = shared_gui.get_camera_frame(main_frame,mqtt_sender)

    return teleopFrame, armFrame, controlFrame, driveSystemFrame, soundmakerFrame, colorFrame, cameraFrame


def grid_frames(teleop_frame, arm_frame, control_frame):
    pass

def get_beepFrame(window,client):
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Sprint 2 things")

    driveButton = ttk.Button(frame, text="Drive")
    targetButton = ttk.Button(frame, text='Target')
    initBox = ttk.Entry(frame,width=8)
    rateBox = ttk.Entry(frame,width=8)
    initBox.insert(0,'1')
    rateBox.insert(0,'1')

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    driveButton.grid(row=2,column=0)
    initBox.grid(row=2,column=1)
    rateBox.grid(row=2,column=2)
    targetButton.grid(row=3,column=0)

    # Set the button callbacks:
    driveButton['command'] = lambda: handleBeepDrive(client,initBox,rateBox)
    targetButton['command'] = lambda: handleTarget(client)

    return frame

def getSimonFrame(window,client):

    Frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    Frame.grid()

    frameLabel = ttk.Label(Frame,text='Simon Says')
    simonButton = ttk.Button(Frame,text='Simon Says...')
    moveButton = ttk.Button(Frame,text='Move')
    moveBox = ttk.Entry(Frame,width=8)
    moveBox.insert(0,'5')
    moveText = ttk.Label(Frame,text='Inches:')
    danceButton = ttk.Button(Frame,text='Dance!')
    stretchButton = ttk.Button(Frame,text='Stretch')
    liftButton = ttk.Button(Frame,text='Lift')
    findButton = ttk.Button(Frame,text='Find Cube')
    blankLabel= ttk.Label(Frame,text='')
    blankLabel2 = ttk.Label(Frame,text='')
    diffLabel = ttk.Label(Frame,text='Difficulty Bar')
    difficultBar = ttk.Progressbar(Frame,maximum=1000)
    difficultBar.step(40)

    frameLabel.grid(row=0,column=1)
    blankLabel.grid(row=1,column=1)
    simonButton.grid(row=2,column=1)
    blankLabel2.grid(row=3,column=1)
    moveButton.grid(row=4,column=0)
    moveText.grid(row=4,column=1)
    moveBox.grid(row=4,column=2)
    danceButton.grid(row=5,column=0)
    stretchButton.grid(row=6,column=0)
    liftButton.grid(row=7,column=0)
    findButton.grid(row=8,column=0)
    diffLabel.grid(row=9,column=1)
    difficultBar.grid(row=10,column=1)

    return Frame

def handleBeepDrive(client,box1,box2):

    client.send_message('m1BeepDrive',[box1.get(),box2.get()])

def handleTarget(client):

    client.send_message('centerOnTarget')
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()


