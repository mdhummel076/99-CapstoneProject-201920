"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and James Werne, Matt Hummel, and Luke Spannan.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time



def get_perform_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has a Button object that tells the robot to navigate the stage and
    perform the song, then leave the stage.
    :param window:
    :param mqtt_sender:
    :return: frame
    """

    # Construct frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")

    # Construct widgets
    frame_label = ttk.Label(frame, text="Performance Options")

    perform_button = ttk.Button(frame, text='Perform Song')
    enter_stage_button = ttk.Button(frame, text='Enter Stage')
    exit_stage_button = ttk.Button(frame, text='Exit Stage')

    # Grid widgets
    frame_label.grid(row=0, column=0)
    perform_button.grid(row=2, column=0)
    enter_stage_button.grid(row=3, column=0)
    exit_stage_button.grid(row=4, column=0)

    # Define Handlers

    perform_button['command'] = lambda: handle_perform_button(window, mqtt_sender)
    enter_stage_button['command'] = lambda: handle_enter_stage_button(window, mqtt_sender)
    exit_stage_button['command'] = lambda: handle_exit_stage_button(window, mqtt_sender)




    return frame



def handle_perform_button(window, mqtt_sender):
    print('Perform Song')
    mqtt_sender.send_message('perform', [window, mqtt_sender])


def handle_enter_stage_button(window, mqtt_sender):
    print('Enter Stage - go to the spotlight')
    yellow = 4
    mqtt_sender.send_message('enter_stage', [yellow])

def handle_exit_stage_button(window, mqtt_sender):
    print('Exit Stage - back to the shadows')
    mqtt_sender.send_message('exit_stage')

def handle_check_anxiety():
    print('Checking anxiety levels')
    mqtt_sender.send_message('check_anxiety')




def encore_text(self, frame):
    label = ttk.Label(frame, text='Encore:')
    quote1 = ttk.Label(frame, text='Congratulations!')
    quote2 = ttk.Label(frame, text='The crowd loves you,')
    quote3 = ttk.Label(frame, text="and you're feeling good.")
    quote4 = ttk.Label(frame, text="Time for an encore!")

    label.grid(row=5, column=0)
    quote1.grid(row=6, column=0)
    quote2.grid(row=7, column=0)
    quote3.grid(row=8, column=0)
    quote4.grid(row=9, column=0)


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    return frame


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame


def get_drivesystem_frame(window, mqtt_sender):

    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")

    frame_label = ttk.Label(frame, text="DriveSystem")

    # Construct widgets for frame
    drive_using_seconds_button = ttk.Button(frame, text="Go Straight For Seconds")
    drive_seconds_label = ttk.Label(frame, text="Desired travel time:")
    drive_speed_label1 = ttk.Label(frame, text="Desired speed:")
    drive_seconds_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    drive_seconds_entry.insert(0, "2")
    drive_speed_entry1 = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    drive_speed_entry1.insert(0, "100")

    drive_inches_using_time_button = ttk.Button(frame, text="Go Straight For Inches Using Time")
    drive_inches_label1 = ttk.Label(frame, text="Desired travel distance (inches):")
    drive_speed_label2 = ttk.Label(frame, text="Desired speed:")
    drive_inches_entry1 = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    drive_inches_entry1.insert(0, "5")
    drive_speed_entry2 = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    drive_speed_entry2.insert(0, "100")

    drive_encoder_button = ttk.Button(frame, text="Go Straight For Inches Using Encoder")
    drive_inches_label2 = ttk.Label(frame, text="Desired travel distance (inches):")
    drive_speed_label3 = ttk.Label(frame, text="Desired speed:")
    drive_inches_entry2 = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    drive_inches_entry2.insert(0, "5")
    drive_speed_entry3 = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    drive_speed_entry3.insert(0, "100")

    frame_label.grid(row=0, column=0)
    drive_using_seconds_button.grid(row=1, column=0)
    drive_seconds_label.grid(row=2, column=0)
    drive_speed_label1.grid(row=3, column=0)
    drive_seconds_entry.grid(row=2, column=1)
    drive_speed_entry1.grid(row=3, column=1)

    drive_inches_using_time_button.grid(row=4, column=0)
    drive_inches_label1.grid(row=5, column=0)
    drive_speed_label2.grid(row=6, column=0)
    drive_inches_entry1.grid(row=5, column=1)
    drive_speed_entry2.grid(row=6, column=1)

    drive_encoder_button.grid(row=7, column=0)
    drive_inches_label2.grid(row=8, column=0)
    drive_speed_label3.grid(row=9, column=0)
    drive_inches_entry2.grid(row=8, column=1)
    drive_speed_entry3.grid(row=9, column=1)

    drive_using_seconds_button["command"] = lambda: handle_go_straight_for_seconds(
        drive_seconds_entry, drive_speed_entry1, mqtt_sender)
    drive_inches_using_time_button["command"] = lambda: handle_go_straight_for_inches_using_time(
        drive_inches_entry1, drive_speed_entry2, mqtt_sender)
    drive_encoder_button["command"] = lambda: handle_go_straight_for_inches_using_encoder(
        drive_inches_entry2, drive_speed_entry3, mqtt_sender)

    return frame

def get_soundmaker_frame(window,mqtt_sender):

    Frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")

    beepButton = ttk.Button(Frame, text='Beep')
    beepBox = ttk.Entry(Frame, width=8, justify=tkinter.RIGHT)
    beepBox.insert(0, '1')
    toneButton = ttk.Button(Frame, text='Tone')
    toneBox = ttk.Entry(Frame, width=8, justify=tkinter.RIGHT)
    toneBox.insert(0,'440')
    durationBox = ttk.Entry(Frame, width=8, justify=tkinter.RIGHT)
    durationBox.insert(0,'2000')
    speakButton = ttk.Button(Frame,text='Speak')
    speakBox = ttk.Entry(Frame, width=8, justify=tkinter.RIGHT)
    speakBox.insert(0,'Hello')

    beepButton.grid(row=0,column=0)
    beepBox.grid(row=0,column=1)
    toneButton.grid(row = 1,column=0)
    toneBox.grid(row=1,column=1)
    durationBox.grid(row=1,column=2)
    speakButton.grid(row=2,column=0)
    speakBox.grid(row=2,column=1)

    beepButton['command']=lambda: handle_beep(mqtt_sender,beepBox)
    toneButton['command']=lambda : handle_tone(mqtt_sender,toneBox,durationBox)
    speakButton['command']=lambda: handle_speak(mqtt_sender,speakBox)

    return Frame




def get_ColorSensor_Frame(window, mqtt_sender):

    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")

    frame_label = ttk.Label(frame, text="Color Sensor Methods")
    speed_label = ttk.Label(frame, text="Desired Speed:")
    speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    intensity_label = ttk.Label(frame, text="Desired Intensity:")
    intensity_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)


    go_straight_intensity_less_than_button = ttk.Button(frame, text="Go Straight Until Intensity Is Less Than")

    go_straight_intensity_greater_than_button = ttk.Button(frame, text="Go Straight Until Intensity Is Greater Than")

    color_label = ttk.Label(frame, text="Enter Color:")
    color_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)

    go_straight_until_color_is_button = ttk.Button(frame, text="Go Straight Until Color Is")
    go_straight_until_color_is_not_button = ttk.Button(frame, text="Go Straight Until Color Is Not")

    frame_label.grid(row=0, column=0)
    speed_label.grid(row=1, column=0)
    speed_entry.grid(row=1, column=1)
    intensity_label.grid(row=2, column=0)
    intensity_entry.grid(row=2, column=1)
    color_label.grid(row=3, column=0)
    color_entry.grid(row=3, column=1)

    go_straight_intensity_less_than_button.grid(row=4, column=0)
    go_straight_intensity_greater_than_button.grid(row=5, column=0)
    go_straight_until_color_is_button.grid(row=4, column=1)
    go_straight_until_color_is_not_button.grid(row=5, column=1)

    go_straight_intensity_less_than_button['command']=lambda: handle_intensity_less_than(
        speed_entry, intensity_entry, mqtt_sender)
    go_straight_intensity_greater_than_button['command']=lambda: handle_intensity_greater_than(
        speed_entry, intensity_entry, mqtt_sender)
    go_straight_until_color_is_button['command']=lambda: handle_color_is(
        color_entry, speed_entry, mqtt_sender)
    go_straight_until_color_is_not_button['command']=lambda: handle_color_is_not(
        color_entry, speed_entry, mqtt_sender)

    return frame

def get_camera_frame(window,client):
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Camera")

    dataButton = ttk.Button(frame, text="Print Data")
    cwButton = ttk.Button(frame, text="Look Clockwise")
    ccwButton = ttk.Button(frame, text="Look Counter-Clockwise")
    speedBox = ttk.Entry(frame, width=8)
    speedBox.insert(0, '100')
    areaBox = ttk.Entry(frame, width=8)
    areaBox.insert(0, '100')

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    dataButton.grid(row=1, column=0)
    cwButton.grid(row=1, column=1)
    ccwButton.grid(row=1, column=2)
    speedBox.grid(row=2, column=1)
    areaBox.grid(row=2, column=2)

    # Set the button callbacks:
    dataButton['command'] = lambda: printData(client)
    cwButton['command'] = lambda: lookCW(client, speedBox, areaBox)
    ccwButton['command'] = lambda: lookCCW(client, speedBox, areaBox)

    return frame
def get_IR_Sensor_Frame(window,mqtt_sender):
    frame = ttk.Frame(window,padding =10, borderwidth=5, relief='ridge')
    label = ttk.Label(frame, text='Infrared Sensor Methods')
    label.grid(row=0,column=1)
    speed = ttk.Label(frame, text="Please input speed here" )
    speed.grid(row=1,column=0)
    entry_speed=ttk.Entry(frame,width=8)
    entry_speed.grid(row=2,column=0)
    inches = ttk.Label(frame, text="Please input inches here")
    inches.grid(row=1,column=1)
    entry_inches=ttk.Entry(frame,width=8)
    entry_inches.grid(row=2,column=1)
    delta_inches= ttk.Label(frame,text="Please input delta inches here")
    delta_inches.grid(row=1,column=2)
    entry_delta_inches = ttk.Entry(frame,width=8)
    entry_delta_inches.grid(row=2,column=2)
    Lesser = ttk.Button(frame, text='Go forward until distance is less than')
    Lesser.grid(row=3,column=0)
    Greater = ttk.Button(frame, text = "Go backwards until distance is greater than")
    Greater.grid(row=3,column=1)
    Delta = ttk.Button(frame, text = "Go until distance is within")
    Delta.grid(row=3,column=2)

    Delta['command'] = lambda: handle_go_until_distance_is_within(entry_delta_inches,entry_speed,mqtt_sender)
    Greater['command'] = lambda: handle_go_backward_until_distance_is_greater_than(entry_inches,entry_speed,mqtt_sender)
    Lesser['command'] = lambda: handle_go_forward_until_distance_is_less_than(entry_inches,entry_speed,mqtt_sender)

    return frame


###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('Drive forward')
    mqtt_sender.send_message('go',[int(left_entry_box.get()),int(right_entry_box.get())])


def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('Drive backward')
    mqtt_sender.send_message('go',[-1*int(left_entry_box.get()),-1*int(right_entry_box.get())])


def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('Move left')
    mqtt_sender.send_message('go',[-1*int(left_entry_box.get()),int(right_entry_box.get())])



def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('Move right')
    mqtt_sender.send_message('go',[int(left_entry_box.get()),-1*int(right_entry_box.get())])


def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Stop')
    mqtt_sender.send_message('stop')

def handle_go_straight_for_seconds(seconds_entry_box, speed_entry_box, mqtt_sender):
    print('Go straight for ', seconds_entry_box.get(), 'seconds')
    mqtt_sender.send_message('go_straight_for_seconds', [int(seconds_entry_box.get()), int(speed_entry_box.get())])

def handle_go_straight_for_inches_using_time(inches_entry_box, speed_entry_box, mqtt_sender):
    print('Go straight for ', inches_entry_box.get(), 'inches')
    mqtt_sender.send_message('go_straight_for_inches_using_time', [int(inches_entry_box.get()), int(speed_entry_box.get())])

def handle_go_straight_for_inches_using_encoder(inches_entry_box, speed_entry_box, mqtt_sender):
    print('Go straight for ', inches_entry_box, 'inches (using encoder)')
    mqtt_sender.send_message('go_straight_for_inches_using_encoder', [int(inches_entry_box.get()), int(speed_entry_box.get())])

###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed
      :type  mqtt_sender:  com.MqttClient
    """
    print('Raise Arm')
    mqtt_sender.send_message('raise_arm')


def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Lower Arm')
    mqtt_sender.send_message('lower_arm')


def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Calibrate Arm')
    mqtt_sender.send_message('calibrate_arm')


def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print('Move Arm to Position', arm_position_entry.get())
    mqtt_sender.send_message('move_arm_to_position',[arm_position_entry.get()])


###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """

    mqtt_sender.send_message('quit')


def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    mqtt_sender.send_message('quit')

    time.sleep(1)

    exit()


#handlers for sounds

def handle_beep(mqtt_sender, entryBox):
    print('I will beep ', entryBox.get(), 'times')
    mqtt_sender.send_message('beep',[entryBox.get()])

def handle_tone(mqtt_sender, entryBox, entryBox2):
    print('I will play a tone at frequency ', entryBox.get(), 'for duration ', entryBox.get())
    mqtt_sender.send_message('tone',[entryBox.get(),entryBox2.get()])

def handle_speak(mqtt_sender, entryBox):
    print('I will speak phrase ', entryBox.get())
    mqtt_sender.send_message('speak',[entryBox.get()])

# Handlers for Color Methods

def handle_intensity_less_than(speed_entry, intensity_entry, mqtt_sender):
    print('Go Straight at a speed of', speed_entry.get(), 'until intensity is less than', intensity_entry.get())
    mqtt_sender.send_message('go_straight_until_intensity_is_less_than', [intensity_entry.get(), speed_entry.get()])

def handle_intensity_greater_than(speed_entry, intensity_entry, mqtt_sender):
    print('Go Straight at a speed of', speed_entry.get(), 'until intensity is greater than', intensity_entry.get())
    mqtt_sender.send_message('go_straight_until_intensity_is_greater_than', [intensity_entry.get(), speed_entry.get()])

def handle_color_is(color_entry, speed_entry, mqtt_sender):
    print('Go straight at speed of', speed_entry.get(), 'until color is', color_entry.get())
    mqtt_sender.send_message('go_straight_until_color_is', [color_entry.get(), speed_entry.get()])

def handle_color_is_not(color_entry, speed_entry, mqtt_sender):
    print('Go straight at speed of', speed_entry.get(), 'until color is not', color_entry.get())
    mqtt_sender.send_message('go_straight_until_color_is_not', [color_entry.get(), speed_entry.get()])

def printData(client):

    client.send_message('printData')

def lookCW(client,box1,box2):

    client.send_message('CW',[box1.get(),box2.get()])

def lookCCW(client,box1,box2):

    client.send_message('CCW',[box1.get(),box2.get()])

def handle_go_forward_until_distance_is_less_than(entry_inches,entry_speed,mqtt_sender):
    print('Go at speed',entry_speed.get(),'for',entry_inches.get())
    mqtt_sender.send_message('go_forward_until_distance_is_less_than',[entry_inches.get(), entry_speed.get()])

def handle_go_backward_until_distance_is_greater_than(entry_inches,entry_speed,mqtt_sender):
    print('Go backwards at speed',entry_speed.get(),'for',entry_inches.get())
    mqtt_sender.send_message('go_backward_until_distance_is_greater_than',[entry_inches.get(), entry_speed.get()])

def handle_go_until_distance_is_within(entry_delta_inches,entry_speed,mqtt_sender):
    print("Go at speed", entry_speed.get(), "within a distance of", entry_delta_inches.get())
    mqtt_sender.send_message('go_until_distance_is_within', [entry_delta_inches.get(), entry_speed.get()])

