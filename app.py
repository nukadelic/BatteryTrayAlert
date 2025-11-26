import pystray
import PIL.Image
import tkinter as tk
from tkinter import messagebox

from io import BytesIO
import base64

import psutil

import threading
import time

alert_message_active = True

def is_plugged_in():
    if psutil.sensors_battery() is None : # always return true if there is no battery ... 
        return True
    return psutil.sensors_battery().power_plugged 

def check_wallplug():
    
    global alert_message_active

    last_battery_status = True

    while True:
        plugged_in = is_plugged_in()
        if not plugged_in == last_battery_status :
            last_battery_status = plugged_in
            if not plugged_in :
                
                if alert_message_active : 
                    messagebox.showinfo("ALERT", "BATTERY DISCONNECTED ! ! ")

        time.sleep(1)


def on_exit(icon):
    icon.stop()

def on_action():
    messagebox.showinfo("Action", "You clicked an action!")

# embeded png ( https://www.base64-image.de/ ) 
img_data = base64.b64decode("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")
image = PIL.Image.open(BytesIO(img_data))

def toggle_alert_active():
    global alert_message_active
    alert_message_active = not alert_message_active
    return alert_message_active

# Create a menu
menu = pystray.Menu(
    pystray.MenuItem(
        "Alert Popup Enabled", 
        toggle_alert_active,
        checked=lambda item: alert_message_active
    ),
    pystray.MenuItem("Exit", on_exit)
)

# Create the system tray icon
icon = pystray.Icon("name", image, "Tray Batery Alert", menu)

if psutil.sensors_battery() is not None :

    # Create the background thread
    time_thread = threading.Thread(target=check_wallplug, daemon=True)
    time_thread.start()

    # Run the icon
    icon.run()
