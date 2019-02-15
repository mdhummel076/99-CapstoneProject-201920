# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk

import ev3dev.ev3 as ev3
import time
import math

def main():

    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    root = tkinter.Tk()
    root.title("Capstone Project - James")

    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()

    decision = [0]





    first_button = ttk.Button(main_frame, text="Generate new button")
    first_button.grid(row=0,column=0)
    x = 3
    if x > 2:
        label = ttk.Label(main_frame, text='Encore!')
        quote1 = ttk.Label(main_frame, text='Congratulations!')
        quote2 = ttk.Label(main_frame, text='The crowd loves you,')
        quote3 = ttk.Label(main_frame, text="and you're feeling good.")
        quote4 = ttk.Label(main_frame, text="Time for an encore!")

        label.grid(row=5, column=0)
        quote1.grid(row=6, column=0)
        quote2.grid(row=7, column=0)
        quote3.grid(row=8, column=0)
        quote4.grid(row=9, column=0)
        time.sleep(5)

    root.mainloop()



def encore_prompt(root, main_frame, mqtt_sender, decision):

    # Construct widgets
    encore_label = ttk.Label(main_frame, text="Encore?")
    yes_button = ttk.Button(main_frame, text='Yes')
    no_button = ttk.Button(main_frame, text='No')

    # Grid widgets
    encore_label.grid(row=5, column=0)
    yes_button.grid(row=6, column=0)
    no_button.grid(row=6, column=1)

    time.sleep(2)
    yes_button['command'] = lambda: true(decision)
    no_button['command'] = lambda: false(decision)
    time.sleep(2)
    yes_button['command'] = lambda: true(decision)
    no_button['command'] = lambda: false(decision)
    time.sleep(2)

    if decision[0] == 'True':
        encore()
        yes_button.destroy()
        no_button.destroy()
        return True
    elif decision[0] == 'False':
        print('False -- read!')
        return False
    root.mainloop()

def true(decision):
    decision[0] = 'True'

def false(decision):
    decision[0] = 'False'


main()