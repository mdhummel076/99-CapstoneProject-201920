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
import m2_gui
import rosebot
import time


class MyDelegate(object):
    """ Constructs PC delegate object. Has
    handlers for changing anxiety, changing
    hostility levels, and for printing on the
    console (for troubleshooting purposes)"""

    def __init__(self):
        self.enabled = True

    def handle_change_anxiety(self, distance):
        m2_gui.change_anxiety(int(distance))

    def handle_change_hostility(self):
        m2_gui.change_hostility()

    def print_on_pc(self, message):
        print(str(message))


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    # Creates mqtt sender to call methods on robot
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    # Created pc delegate, then used it as object to receive messages from robot
    pc_delegate = MyDelegate()
    mqtt_receiver = com.MqttClient(pc_delegate)
    mqtt_receiver.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    # Created tkinter window
    root = tkinter.Tk()
    root.title("Capstone Project - James")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    # Established primary frame & gridded it
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the m2_GUI
    # -------------------------------------------------------------------------
    # Called other frames using get_shared_frames method
    perform_frame, teleop_frame, arm_frame, control_frame, drivesystem_frame, soundmaker_frame = get_shared_frames(
        main_frame, mqtt_sender)

    # sprint_2_frame = sprint_2_frames(main_frame, mqtt_sender)
    # sprint_2_1_frame = sprint_3_frames(main_frame, mqtt_sender)
    # grid_frames(teleop_frame, arm_frame, control_frame, drivesystem_frame, soundmaker_frame, IR_Frame, color_sensor_frame,
    # cameraFrame, sprint_2_frame, sprint_2_1_frame)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------

    # Grids frames for Sprint 3
    real_grid_frames(perform_frame, teleop_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------

    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    perform_frame = m2_gui.get_perform_frame(main_frame, mqtt_sender)
    teleop_frame = m2_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = m2_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = m2_gui.get_control_frame(main_frame, mqtt_sender)
    drivesystem_frame = m2_gui.get_drivesystem_frame(main_frame, mqtt_sender)
    soundmaker_frame = m2_gui.get_soundmaker_frame(main_frame, mqtt_sender)

    return perform_frame, teleop_frame, arm_frame, control_frame, drivesystem_frame, soundmaker_frame


def grid_frames(teleop_frame, arm_frame, control_frame, drivesystem_frame, soundmaker_frame, IR_Frame,
                color_sensor_frame,
                cameraFrame, sprint_2_frame, sprint_2_1_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    drivesystem_frame.grid(row=0, column=1)
    soundmaker_frame.grid(row=1, column=1)
    IR_Frame.grid(row=4, column=1)
    color_sensor_frame.grid(row=2, column=1)
    cameraFrame.grid(row=3, column=0)
    sprint_2_frame.grid(row=3, column=1)
    sprint_2_1_frame.grid(row=4, column=0)


def real_grid_frames(perform_frame, teleop_frame):
    # Grids frames for Sprint 3

    perform_frame.grid(row=0, column=0)
    teleop_frame.grid(row=1, column=0)


# -------- Sprint 1-2 Code: ---------#


def handle_robot_proximity_tone(frequency_entry, inc_frequency_entry, mqtt_sender):
    print('Start at', frequency_entry.get(), 'Hz, then increase by', inc_frequency_entry.get(), "Hz per inch")
    mqtt_sender.send_message('robot_proximity_tone', [int(frequency_entry.get()), int(inc_frequency_entry.get())])


def handle_robot_point_to_object(mqtt_sender):
    print('Make Robot Point to Object')
    mqtt_sender.send_message('robot_point_to_object')


def handle_robot_proximity_led(frequency_entry, inc_frequency_entry, mqtt_sender):
    print('Start at', frequency_entry.get(), 'cycles per sec, then increase by', inc_frequency_entry.get(),
          "cycles per inch")
    mqtt_sender.send_message('robot_proximity_led', [int(frequency_entry.get()), int(inc_frequency_entry.get())])


def handle_camera_proximity_led(mqtt_sender):
    print('Go to object & blink while driving')
    mqtt_sender.send_message('camera_proximity_led')


def sprint_2_frames(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")

    frame_label = ttk.Label(frame, text="Sprint 2: Feature 9 & 10")
    frame_label.grid(row=0, column=0)

    robot_proximity_tone_button = ttk.Button(frame, text="Make Tones Frequency Increase with Proximity")
    robot_proximity_tone_button.grid(row=4, column=0)
    robot_frequency_label = ttk.Label(frame, text="Start Frequency:")
    robot_frequency_entry_box = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    robot_inc_frequency_label = ttk.Label(frame, text="Frequency Rate of Increase")
    robot_inc_frequency_entry_box = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)

    robot_frequency_label.grid(row=5, column=0)
    robot_frequency_entry_box.grid(row=5, column=1)
    robot_frequency_entry_box.insert(0, '440')
    robot_inc_frequency_label.grid(row=6, column=0)
    robot_inc_frequency_entry_box.grid(row=6, column=1)
    robot_inc_frequency_entry_box.insert(0, 20)

    robot_point_to_object_button = ttk.Button(frame, text="Make Robot Point Straight to Object")
    robot_point_to_object_button.grid(row=7, column=0)

    robot_proximity_tone_button['command'] = lambda: handle_robot_proximity_tone(
        robot_frequency_entry_box, robot_inc_frequency_entry_box, mqtt_sender)
    robot_point_to_object_button['command'] = lambda: handle_robot_point_to_object(mqtt_sender)

    return frame


def sprint_3_frames(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")

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

    robot_proximity_led_button['command'] = lambda: handle_robot_proximity_led(
        robot_frequency_entry_box, robot_inc_frequency_entry_box, mqtt_sender)
    robot_camera_proximity_led_button['command'] = lambda: handle_camera_proximity_led(mqtt_sender)

    return frame


def printData(client):
    client.send_message('printData')


def lookCW(client, box1, box2):
    client.send_message('CW', [box1.get(), box2.get()])


def lookCCW(client, box1, box2):
    client.send_message('CCW', [box1.get(), box2.get()])


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
