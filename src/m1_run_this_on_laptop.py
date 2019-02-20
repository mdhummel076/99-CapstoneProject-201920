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
import random


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    delegate = laptopDelegate()
    client = com.MqttClient(delegate)
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
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------

    simonFrame, textBox = getSimonFrame(mainFrame,client)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------

    simonFrame.grid(row=0,column=0)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------

    delegate.gui = textBox
    root.mainloop()

    #Creates the frame with all the simon says functionality
def getSimonFrame(window,client):

    Frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    Frame.grid()

    frameLabel = ttk.Label(Frame,text='Simon Says')
    simonButton = ttk.Button(Frame,text='Simon Says...')
    moveButton = ttk.Button(Frame,text='Move')
    danceButton = ttk.Button(Frame,text='Dance!')
    stretchButton = ttk.Button(Frame,text='Stretch')
    clapButton = ttk.Button(Frame,text='Clap')
    colorButton = ttk.Button(Frame,text='Read Color')
    findButton = ttk.Button(Frame,text='Find Cube')
    beepButton = ttk.Button(Frame,text='Beep')
    singButton = ttk.Button(Frame,text='Sing')
    blankLabel= ttk.Label(Frame,text='')
    blankLabel2 = ttk.Label(Frame,text='')
    diffLabel = ttk.Label(Frame,text='Difficulty Bar')
    difficultBar = ttk.Progressbar(Frame,maximum=1000)
    difficultBar.start(200)
    difficultBar.step(1)
    textBox = ttk.Entry(Frame)
    textBox.insert(0,'Ready to play!')
    winBox = ttk.Entry(Frame)

    frameLabel.grid(row=0,column=1)
    blankLabel.grid(row=1,column=1)
    simonButton.grid(row=2,column=1)
    blankLabel2.grid(row=3,column=1)
    moveButton.grid(row=4,column=0)
    danceButton.grid(row=5,column=0)
    stretchButton.grid(row=6,column=0)
    clapButton.grid(row=7,column=0)
    colorButton.grid(row=4,column=2)
    findButton.grid(row=5,column=2)
    beepButton.grid(row=6,column=2)
    singButton.grid(row=7,column=2)
    diffLabel.grid(row=11,column=1)
    difficultBar.grid(row=12,column=1)
    textBox.grid(row=13,column=1)
    winBox.grid(row=14,column=1)

    simonButton['command'] = lambda: handleSimon(client, difficultBar, textBox, winBox)
    moveButton['command'] = lambda: handleMove(client, difficultBar, textBox, winBox)
    danceButton['command'] = lambda: handleDance(client, difficultBar, textBox, winBox)
    stretchButton['command'] = lambda: handleStretch(client, difficultBar, textBox, winBox)
    clapButton['command'] = lambda: handleClap(client, difficultBar, textBox, winBox)
    colorButton['command'] = lambda: handleColor(client, difficultBar, textBox, winBox)
    findButton['command'] = lambda: handleFind(client, difficultBar, textBox, winBox)
    beepButton['command'] = lambda: handleBeep(client, difficultBar, textBox, winBox)
    singButton['command'] = lambda: handleSing(client, difficultBar, textBox, winBox)


    return Frame, textBox

    #Creates a function to handle each button press event and communicate the desired action to the robot's Delegate
def handleSimon(client, difficultBar, textBox, winBox):
    textBox.delete(0,100)
    textBox.insert(0,'Simon Says...')

def handleMove(client, difficultBar, textBox, winBox):

    difficultBar.step(10)
    if textBox.get() == 'Simon Says...':
        textBox.delete(0, 100)
        textBox.insert(0, 'Moving')
        client.send_message('Move')
    elif doesFail(difficultBar):
        textBox.delete(0,100)
        textBox.insert(0, 'Whoops!')
        client.send_message('Move')
        winBox.delete(0, 100)
        winBox.insert(0,'You Win!')
        difficultBar.stop()
    else:
        textBox.delete(0, 100)
        textBox.insert(0, 'Waiting...')

def handleDance(client, difficultBar, textBox, winBox):

    difficultBar.step(10)
    if textBox.get() == 'Simon Says...':
        textBox.delete(0, 100)
        textBox.insert(0, 'Dancing')
        client.send_message('Dance')
    elif doesFail(difficultBar):
        textBox.delete(0, 100)
        textBox.insert(0, 'Whoops!')
        client.send_message('Dance')
        winBox.delete(0, 100)
        winBox.insert(0, 'You Win!')
        difficultBar.stop()
    else:
        textBox.delete(0, 100)
        textBox.insert(0, 'Waiting...')

def handleStretch(client, difficultBar, textBox, winBox):

    difficultBar.step(10)
    if textBox.get() == 'Simon Says...':
        textBox.delete(0, 100)
        textBox.insert(0, 'Stretching')
        client.send_message('Stretch')
    elif doesFail(difficultBar):
        textBox.delete(0, 100)
        textBox.insert(0, 'Whoops!')
        client.send_message('Stretch')
        winBox.delete(0, 100)
        winBox.insert(0, 'You Win!')
        difficultBar.stop()
    else:
        textBox.delete(0, 100)
        textBox.insert(0, 'Waiting...')

def handleClap(client, difficultBar, textBox, winBox):

    difficultBar.step(10)
    if textBox.get() == 'Simon Says...':
        textBox.delete(0, 100)
        textBox.insert(0, 'Clapping')
        client.send_message('Clap')
    elif doesFail(difficultBar):
        textBox.delete(0, 100)
        textBox.insert(0, 'Whoops!')
        client.send_message('Clap')
        winBox.delete(0, 100)
        winBox.insert(0, 'You Win!')
        difficultBar.stop()
    else:
        textBox.delete(0, 100)
        textBox.insert(0, 'Waiting...')


def handleColor(client, difficultBar, textBox, winBox):

    difficultBar.step(10)
    if textBox.get() == 'Simon Says...':
        textBox.delete(0, 100)
        textBox.insert(0, 'Looking for Color')
        client.send_message('Color')
    elif doesFail(difficultBar):
        textBox.delete(0, 100)
        textBox.insert(0, 'Whoops!')
        client.send_message('Color')
        winBox.delete(0, 100)
        winBox.insert(0, 'You Win!')
        difficultBar.stop()
    else:
        textBox.delete(0, 100)
        textBox.insert(0, 'Waiting...')

def handleFind(client, difficultBar, textBox, winBox):

    difficultBar.step(10)
    if textBox.get() == 'Simon Says...':
        textBox.delete(0, 100)
        textBox.insert(0, 'Finding')
        client.send_message('Find')
    elif doesFail(difficultBar):
        textBox.delete(0, 100)
        textBox.insert(0, 'Whoops!')
        client.send_message('Find')
        winBox.delete(0, 100)
        winBox.insert(0, 'You Win!')
        difficultBar.stop()
    else:
        textBox.delete(0, 100)
        textBox.insert(0, 'Waiting...')

def handleBeep(client, difficultBar, textBox, winBox):

    difficultBar.step(10)
    if textBox.get() == 'Simon Says...':
        textBox.delete(0, 100)
        textBox.insert(0, 'Beeping')
        client.send_message('Beep')
    elif doesFail(difficultBar):
        textBox.delete(0, 100)
        textBox.insert(0, 'Whoops!')
        client.send_message('Beep')
        winBox.delete(0, 100)
        winBox.insert(0, 'You Win!')
        difficultBar.stop()
    else:
        textBox.delete(0, 100)
        textBox.insert(0, 'Waiting...')

def handleSing(client, difficultBar, textBox, winBox):

    difficultBar.step(10)
    if textBox.get() == 'Simon Says...':
        textBox.delete(0, 100)
        textBox.insert(0, 'Singing')
        client.send_message('Sing')
    elif doesFail(difficultBar):
        textBox.delete(0, 100)
        textBox.insert(0, 'Whoops!')
        client.send_message('Sing')
        winBox.delete(0, 100)
        winBox.insert(0, 'You Win!')
        difficultBar.stop()
    else:
        textBox.delete(0, 100)
        textBox.insert(0, 'Waiting...')

def doesFail(difficultBar):

    difficultBar.step(5)
    num = random.randrange(0,100)
    diffCo = difficultBar['value']/1000 + 1

    return num*diffCo>95

    #Create the delegate to recieve robot data on the laptop. Basically just posts robot data to the GUI text box
class laptopDelegate(object):

    def __init__(self):

        self.gui = None

    def writeText(self,text):

        self.gui.delete(0,100)
        self.gui.insert(0,text)



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()


