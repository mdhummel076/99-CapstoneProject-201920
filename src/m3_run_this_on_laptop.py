"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Luke Spannan.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


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


    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("CSSE120 Capstone Project")


    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root,  padding = 10, borderwidth = 5, relief = "groove")
    main_frame.grid()


    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop, arm_frame, control_frame, SoundmakerFrame, drive_frame, ColorSensor_Frame, IR_Frame, \
        camera_frame = get_shared_frames(main_frame, client)
    sprint_2_frame = sprint_2_frames(main_frame, client)
    grid_frames(teleop, arm_frame, control_frame, SoundmakerFrame, drive_frame, ColorSensor_Frame, IR_Frame, camera_frame,
                sprint_2_frame)


    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------


    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop = shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame,mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame,mqtt_sender)
    SoundmakerFrame = shared_gui.getSoundmakerFrame(main_frame,mqtt_sender)
    drive_frame = shared_gui.get_drivesystem_frame(main_frame,mqtt_sender)
    ColorSensor_Frame=shared_gui.get_ColorSensor_Frame(main_frame,mqtt_sender)
    IR_Frame = shared_gui.get_IR_Sensor_Frame(main_frame,mqtt_sender)
    camera_frame= shared_gui.get_camera_frame(main_frame,mqtt_sender)

    return teleop, arm_frame, control_frame,SoundmakerFrame,drive_frame,ColorSensor_Frame,IR_Frame,camera_frame


def grid_frames(teleop_frame, arm_frame, control_frame,SoundmakerFrame,drive_frame,ColorSensor_Frame,IR_Frame,camera_frame, sprint_3_frame):
    teleop_frame.grid(row = 0, column =0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    SoundmakerFrame.grid(row=0,column=1)
    drive_frame.grid(row = 0, column = 2)
    ColorSensor_Frame.grid(row=1,column=1)
    IR_Frame.grid(row=1,column=2)
    camera_frame.grid(row=2,column=1)
    sprint_3_frame.grid(row=2, column=2)


def sprint_2_frames(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Sprint 2: Feature 9 & 10")
    frame_label.grid(row=0, column=0)

    robot_proximity_led_button = ttk.Button(frame, text="Make LED blink cycle Increase with Proximity")
    robot_proximity_led_button.grid(row=4, column=0)
    robot_frequency_label = ttk.Label(frame, text="Start Cycle Rate:")
    robot_frequency_entry_box = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    robot_inc_frequency_label = ttk.Label(frame, text="Cycle Rate of Increase")
    robot_inc_frequency_entry_box = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)

    robot_frequency_label.grid(row=5, column=0)
    robot_frequency_entry_box.grid(row=5, column=1)
    robot_frequency_entry_box.insert(0, '2')
    robot_inc_frequency_label.grid(row=6, column=0)
    robot_inc_frequency_entry_box.grid(row=6, column=1)
    robot_inc_frequency_entry_box.insert(0, '2')

    robot_camera_proximity_led_button = ttk.Button(frame, text="Make Robot Go To Object & Blink While Driving")
    robot_camera_proximity_led_button.grid(row=7, column=0)

    robot_proximity_led_button['command']=lambda: handle_robot_proximity_led(
            robot_frequency_entry_box, robot_inc_frequency_entry_box, mqtt_sender)
    robot_camera_proximity_led_button['command']=lambda: handle_camera_proximity_led(mqtt_sender)

    return frame

def handle_robot_proximity_led(frequency_entry, inc_frequency_entry, mqtt_sender):

    print('Start at', frequency_entry.get(), 'cycles per sec, then increase by', inc_frequency_entry.get(), "cycles per inch")
    mqtt_sender.send_message('robot_proximity_led', [int(frequency_entry.get()), int(inc_frequency_entry.get())])

def handle_camera_proximity_led(mqtt_sender):

    print('Go to object & blink while driving')
    mqtt_sender.send_message('camera_proximity_led')


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()