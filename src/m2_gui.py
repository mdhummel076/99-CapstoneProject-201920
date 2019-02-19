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

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import time
import m2_shared_gui_delegate_on_robot
import rosebot

# Global variables used to update *hostility* & *anxiety*
# readings from robot
dis = [8]
anxiety_level = [1]
hostility = ['False']


def get_perform_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has several Button objects that tell the robot to navigate the stage,
    to perform the song (introduction, verse, & chorus), to check anxiety
    levels and crowd hostility levels, and to leave the stage.
    Additionally contains a progress bar that monitors anxiety levels.
    :param window: Tkinter frame
    :param mqtt_sender: MQTTClient object
    :return: frame
    """

    # Construct pc delegate for ev3 to communicate with computer

    # Construct frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")

    # Construct widgets
    frame_label = ttk.Label(frame, text="Performance Options")
    song_label = ttk.Label(frame, text="Setlist:")
    anxiety_label = ttk.Label(frame, text="Anxiety Level:")

    enter_stage_button = ttk.Button(frame, text='Enter Stage')
    exit_stage_button = ttk.Button(frame, text='Exit Stage')
    check_anxiety_button = ttk.Button(frame, text='Check Anxiety')
    check_hostility_button = ttk.Button(frame, text='Check Hostility')

    introduction_button = ttk.Button(frame, text='Introductions')
    verse_button = ttk.Button(frame, text='Verse')
    chorus_button = ttk.Button(frame, text='Chorus')

    # Construct Progress Bar (anxiety measurement)

    s = ttk.Style()
    s.theme_use()
    anxiety_bar = ttk.Progressbar(frame, orient='horizontal', length=100, mode='determinate')
    anxiety_bar.grid(row=10, column=0)
    anxiety_bar['value'] = 50

    # Grid widgets
    frame_label.grid(row=0, column=0, padx=5, pady=5)
    song_label.grid(row=4, column=0, padx=5, pady=5)
    anxiety_label.grid(row=9, column=0, padx=5, pady=5)
    enter_stage_button.grid(row=1, column=0)
    exit_stage_button.grid(row=2, column=0)
    check_anxiety_button.grid(row=3, column=0)
    check_hostility_button.grid(row=4, column=0)

    introduction_button.grid(row=5, column=0)
    verse_button.grid(row=6, column=0)
    chorus_button.grid(row=7, column=0)

    # Define Handlers

    enter_stage_button['command'] = lambda: handle_enter_stage_button(mqtt_sender)
    exit_stage_button['command'] = lambda: handle_exit_stage_button(mqtt_sender)
    check_anxiety_button['command'] = lambda: levels(mqtt_sender, window, frame, anxiety_bar)
    check_hostility_button['command'] = lambda: handle_check_hostility(mqtt_sender)

    # Performance lambda functions
    introduction_button['command'] = lambda: handle_introduction(mqtt_sender)
    verse_button['command'] = lambda: handle_verse(mqtt_sender)
    chorus_button['command'] = lambda: handle_chorus(mqtt_sender, window)

    return frame


def change_anxiety(distance):
    """ Method called in m2_run_this_on_laptop (handle_change_anxiety).
    Updates global variable dis with the proximity sensor value returned
    from 'get_distance_in_inches' method """
    dis[0] = int(distance)


def change_hostility():
    """ Method called in m2_run_this_on_laptop (handle_change_hostility).
    Updates global variable hostility with touch sensor value returned
    from 'is_pressed' method """
    hostility[0] = 'True'


def handle_check_hostility(mqtt_sender):
    """ Handler for checking hostility levels.
    Sends message to robot delegate & runs 'get_touch_press'
    method, which then runs the 'is_pressed' method and updates
    value of 'hostility' variable in m2_gui """

    mqtt_sender.send_message('get_touch_press')
    time.sleep(2)
    print(hostility[0])
    # If touch sensor pressed, robot leaves stage
    if hostility[0] == 'True':
        handle_apology(mqtt_sender)
        print('Apologize to audience')
        time.sleep(2)
        handle_exit_stage_button(mqtt_sender)
        print('Exit Stage')


def levels(mqtt_sender, window, frame, anxiety_bar):
    """ Communicates with delegate on robot & calls 'get_distance_in_inches'
    method, which then prompts robot to update distance variable in m2_gui.
    Updates progress bar based on distance value returned """

    # Used syntax for tkinter progress bar found in this forum:
    # https://stackoverflow.com/questions/13510882/how-to-change-ttk-progressbar-color-in-python
    handle_get_distance_in_inches(mqtt_sender)
    time.sleep(2)

    print(dis[0])
    time.sleep(2)
    # If object is over twelve inches away, anxiety = 0 and anxiety bar empty
    # Updates global variable 'anxiety_level'
    if dis[0] >= 12:
        s = ttk.Style()
        s.theme_use()
        anxiety_level[0] = 0
        anxiety_bar['value'] = 0
        window.update()

        return anxiety_level
    print(dis[0])

    # If object is between 7-12 inches away, anxiety = 1 and anxiety bar half-full
    # Updates global variable 'anxiety_level'
    if dis[0] < 12:
        if dis[0] > 7:
            s = ttk.Style()
            s.theme_use()
            anxiety_level[0] = 1
            anxiety_bar['value'] = 50
            window.update()

            return anxiety_level
    print(dis[0])

    # If object is less than 7 inches away, anxiety = 0 and anxiety bar full & turns red
    # Updates global variable 'anxiety_level'
    # Robot apologizes & leaves stage
    if dis[0] <= 7:
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
        anxiety_bar = ttk.Progressbar(frame, style="red.Horizontal.TProgressbar", orient="horizontal", length=100,
                                      mode="determinate")
        anxiety_level[0] = 2
        anxiety_bar['value'] = 100
        anxiety_bar.grid(row=10, column=0)
        window.update()
        time.sleep(2)

        handle_apology(mqtt_sender)
        print('Apologize to audience')
        time.sleep(2)
        handle_exit_stage_button(mqtt_sender)
        print('Exit Stage')

        return anxiety_level


def handle_enter_stage_button(mqtt_sender):
    """ Handles enter stage function. When button pressed on gui,
    called enter_stage method on robot delegate. Enter stage makes
    robot drive until yellow -- a spotlight -- is reached """
    print('Enter Stage - go to the spotlight')
    yellow = 4
    mqtt_sender.send_message('enter_stage', [yellow])


def handle_exit_stage_button(mqtt_sender):
    """ Handles exit stage function. When button pressed on gui,
    called exit_stage method on robot delegate. Makes robot drive
    until intensity is low (offstage) """
    print('Exit Stage - back to the shadows')
    mqtt_sender.send_message('exit_stage')
    hostility[0] = 'False'


def handle_apology(mqtt_sender):
    """ Handles apology function. When prompted, robot addresses audience
    (via speech) and clumsily creates an excuse to finish show early """
    print('Apologize to the audience')
    mqtt_sender.send_message('apology')


def handle_introduction(mqtt_sender):
    """ Handles introduction function. When button is pressed, robot addresses
    audience (via speech) """
    print('Introductions')
    mqtt_sender.send_message('introduction')


def handle_verse(mqtt_sender):
    """ Handles verse function. When button is pressed, robot *sings*
    verse of song """
    print('Verse')
    mqtt_sender.send_message('verse')


def handle_chorus(mqtt_sender, window):
    """ Handles song function. When button is pressed, robot *sings*
    chorus of song. If anxiety is sufficiently low, robot will follow-up
    with an encore """
    print('Chorus')
    mqtt_sender.send_message('chorus')
    time.sleep(33)
    if anxiety_level[0] == 0:
        encore_text(window)
        time.sleep(5)
        handle_encore(mqtt_sender)


def handle_encore(mqtt_sender):
    """ Handles encore function. When prompted, robot delegate is prompted
    to perform short encore """
    print('Encore')
    mqtt_sender.send_message('encore')


def encore_text(frame):
    """ Updates GUI with text notifying user that an
    encore will be performed """
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


def handle_get_distance_in_inches(mqtt_sender):
    """ Handler for 'get_distance_in_inches' method. Sends message
    to delegate on robot, which then calls 'get_distance_in_inches' method.
    Amount is returned via robot sending message to pc delegate with updated
    distance value """
    print('Get distance in inches')
    mqtt_sender.send_message('get_distance_in_inches')


# -------- Sprints 1-2 ---------#

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


def get_soundmaker_frame(window, mqtt_sender):
    Frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")

    beepButton = ttk.Button(Frame, text='Beep')
    beepBox = ttk.Entry(Frame, width=8, justify=tkinter.RIGHT)
    beepBox.insert(0, '1')
    toneButton = ttk.Button(Frame, text='Tone')
    toneBox = ttk.Entry(Frame, width=8, justify=tkinter.RIGHT)
    toneBox.insert(0, '440')
    durationBox = ttk.Entry(Frame, width=8, justify=tkinter.RIGHT)
    durationBox.insert(0, '2000')
    speakButton = ttk.Button(Frame, text='Speak')
    speakBox = ttk.Entry(Frame, width=8, justify=tkinter.RIGHT)
    speakBox.insert(0, 'Hello')

    beepButton.grid(row=0, column=0)
    beepBox.grid(row=0, column=1)
    toneButton.grid(row=1, column=0)
    toneBox.grid(row=1, column=1)
    durationBox.grid(row=1, column=2)
    speakButton.grid(row=2, column=0)
    speakBox.grid(row=2, column=1)

    beepButton['command'] = lambda: handle_beep(mqtt_sender, beepBox)
    toneButton['command'] = lambda: handle_tone(mqtt_sender, toneBox, durationBox)
    speakButton['command'] = lambda: handle_speak(mqtt_sender, speakBox)

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

    go_straight_intensity_less_than_button['command'] = lambda: handle_intensity_less_than(
        speed_entry, intensity_entry, mqtt_sender)
    go_straight_intensity_greater_than_button['command'] = lambda: handle_intensity_greater_than(
        speed_entry, intensity_entry, mqtt_sender)
    go_straight_until_color_is_button['command'] = lambda: handle_color_is(
        color_entry, speed_entry, mqtt_sender)
    go_straight_until_color_is_not_button['command'] = lambda: handle_color_is_not(
        color_entry, speed_entry, mqtt_sender)

    return frame


def get_camera_frame(window, client):
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


def get_IR_Sensor_Frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='ridge')
    label = ttk.Label(frame, text='Infrared Sensor Methods')
    label.grid(row=0, column=1)
    speed = ttk.Label(frame, text="Please input speed here")
    speed.grid(row=1, column=0)
    entry_speed = ttk.Entry(frame, width=8)
    entry_speed.grid(row=2, column=0)
    inches = ttk.Label(frame, text="Please input inches here")
    inches.grid(row=1, column=1)
    entry_inches = ttk.Entry(frame, width=8)
    entry_inches.grid(row=2, column=1)
    delta_inches = ttk.Label(frame, text="Please input delta inches here")
    delta_inches.grid(row=1, column=2)
    entry_delta_inches = ttk.Entry(frame, width=8)
    entry_delta_inches.grid(row=2, column=2)
    Lesser = ttk.Button(frame, text='Go forward until distance is less than')
    Lesser.grid(row=3, column=0)
    Greater = ttk.Button(frame, text="Go backwards until distance is greater than")
    Greater.grid(row=3, column=1)
    Delta = ttk.Button(frame, text="Go until distance is within")
    Delta.grid(row=3, column=2)

    Delta['command'] = lambda: handle_go_until_distance_is_within(entry_delta_inches, entry_speed, mqtt_sender)
    Greater['command'] = lambda: handle_go_backward_until_distance_is_greater_than(entry_inches, entry_speed,
                                                                                   mqtt_sender)
    Lesser['command'] = lambda: handle_go_forward_until_distance_is_less_than(entry_inches, entry_speed, mqtt_sender)

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
    mqtt_sender.send_message('go', [int(left_entry_box.get()), int(right_entry_box.get())])


def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('Drive backward')
    mqtt_sender.send_message('go', [-1 * int(left_entry_box.get()), -1 * int(right_entry_box.get())])


def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('Move left')
    mqtt_sender.send_message('go', [-1 * int(left_entry_box.get()), int(right_entry_box.get())])


def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('Move right')
    mqtt_sender.send_message('go', [int(left_entry_box.get()), -1 * int(right_entry_box.get())])


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
    mqtt_sender.send_message('go_straight_for_inches_using_time',
                             [int(inches_entry_box.get()), int(speed_entry_box.get())])


def handle_go_straight_for_inches_using_encoder(inches_entry_box, speed_entry_box, mqtt_sender):
    print('Go straight for ', inches_entry_box, 'inches (using encoder)')
    mqtt_sender.send_message('go_straight_for_inches_using_encoder',
                             [int(inches_entry_box.get()), int(speed_entry_box.get())])


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
    mqtt_sender.send_message('move_arm_to_position', [arm_position_entry.get()])


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


# handlers for sounds

def handle_beep(mqtt_sender, entryBox):
    print('I will beep ', entryBox.get(), 'times')
    mqtt_sender.send_message('beep', [entryBox.get()])


def handle_tone(mqtt_sender, entryBox, entryBox2):
    print('I will play a tone at frequency ', entryBox.get(), 'for duration ', entryBox.get())
    mqtt_sender.send_message('tone', [entryBox.get(), entryBox2.get()])


def handle_speak(mqtt_sender, entryBox):
    print('I will speak phrase ', entryBox.get())
    mqtt_sender.send_message('speak', [entryBox.get()])


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


def lookCW(client, box1, box2):
    client.send_message('CW', [box1.get(), box2.get()])


def lookCCW(client, box1, box2):
    client.send_message('CCW', [box1.get(), box2.get()])


def handle_go_forward_until_distance_is_less_than(entry_inches, entry_speed, mqtt_sender):
    print('Go at speed', entry_speed.get(), 'for', entry_inches.get())
    mqtt_sender.send_message('go_forward_until_distance_is_less_than', [entry_inches.get(), entry_speed.get()])


def handle_go_backward_until_distance_is_greater_than(entry_inches, entry_speed, mqtt_sender):
    print('Go backwards at speed', entry_speed.get(), 'for', entry_inches.get())
    mqtt_sender.send_message('go_backward_until_distance_is_greater_than', [entry_inches.get(), entry_speed.get()])


def handle_go_until_distance_is_within(entry_delta_inches, entry_speed, mqtt_sender):
    print("Go at speed", entry_speed.get(), "within a distance of", entry_delta_inches.get())
    mqtt_sender.send_message('go_until_distance_is_within', [entry_delta_inches.get(), entry_speed.get()])
