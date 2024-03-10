import os

import pyautogui


def shut_down(time=20):
    cont = "shutdown -s -t %s" % time
    os.system(cont)
    return "Your PC will be turned off within 20 Seconds, 'Stop Shutdown' to Stop the shutdown"

def cancel_shutdown():
    cont = "shutdown /a"
    os.system(cont)
    return "Okay, ShutDown cancelled!"

def hotkey_call(text):
    text = text.split("_")
    text.pop()
    text = tuple(text)
    pyautogui.hotkey(*text)
    return f"Hotkey {text} established successfully!"

def press(text):
    text = text[:text.find("_press")]
    pyautogui.press(text)
    return f"The key {text} has been pressed"

def volume_up(no_times = 1):
    no_times = 5 if no_times < 5 else no_times
    for i in range(no_times):
        pyautogui.press('volumeup')
    return f"Volume has been increased {no_times} times"

def volume_down(no_times = 1):
    no_times = 5 if no_times < 5 else no_times
    for i in range(no_times):
        pyautogui.press('volumedown')
    return f"Volume has been decreased {no_times} times"
