import os, pyautogui
import directory_controller
import whatkit_controller
# Dependencies
# pip install telegram
# pip install python-telegram-bot


class PcController():
    # change to home directory
    directory_controller.find_home_loc()
    
    def __init__(self):
        self.multitask_btn = "mult"

    # def InlineButton(self, update, content):
    #     button_text = [["Pause", "Play"], ["Volume Down", "Mute","Volume Up"], ["Back Forward", "Fast Forward"], "Fullscreen", "Quit", ["Shutdown", "Cancel Shutdown"]]

    # def InlineButton_Hotkeys(self, update, content):
    #     button_text = [["⬅️", "Multitask", "➡️"], "Switch Tabs", ["Previous Workpace", "Next Workspace"], "Close Tab", "Close Window"]
    #     button_reply = [["back forward", "multitask", "fast forward"], "ctrl+tab", ["ctrl+win+left", "ctrl+win+right"], "ctrl+f4", "alt+f4"]

    def ShutDown(self, time1 = 20):
        cont = "shutdown -s -t %s" % time1
        os.system(cont)
        ans =  "Your PC will be turned off within 20 Seconds, 'Stop Shutdown' to Stop the shutdown"
        return ans

    def CancelShutDown(self):
        cont = "shutdown /a"
        os.system(cont)

    def call(self, text):
        self.text = text
        self.CommandCenter()

    def press(self, text):
        text = text[:text.find("_press")]
        pyautogui.press(text)
    def CommandCenter(self):
        text = self.text
        if ("shutdown" or "shut down") == text:
            # text = str(update.message.text).lower()
            sts = self.ShutDown()
            # update.message.reply_text(sts)
        elif "quit" == text:
            quit()
        elif ("play") == text:
            pyautogui.press("space")
        elif "volume" in text:
            if "down" in text:
                pyautogui.press('volumedown')
                # pyautogui.press('volumedown')
                # pyautogui.press('volumedown')
            elif "up" in text:
                pyautogui.press('volumeup')
                # pyautogui.press('volumeup')
                # pyautogui.press('volumeup')
        elif ("press" in text):
            self.press(text)
        elif ("fast forward") == text:
            pyautogui.press("right")
        elif ("back forward") == text:
            pyautogui.press("left")
        elif ("pause") == text:
            pyautogui.press("space")
        elif ("play" in text) and ("play" != text):
            whatkit_controller.YTvideo(text)
        elif "mute" == text:
            pyautogui.press("volumemute")
        elif ("maximize" and "window") in text:
            MaxWindow()
        elif ("fullscreen" in text ) or ("full screen"in text):
            pyautogui.press("f")
        elif ("cancel" and "shutdown") in text:
            self.CancelShutDown()
            update.message.reply_text("Okay, ShutDown cancelled!")
        elif ("stop" and "shutdown") in text:
            CancelShutDown()
            update.message.reply_text("Okay, ShutDown cancelled!")
        elif "ctrl+tab" == text:
            pyautogui.hotkey("ctrl", "tab")
        elif "multitask" == text:
            if self.multitask_btn == "mult":
                pyautogui.hotkey("ctrl", "alt", "tab")
                self.multitask_btn = "selt"
            else:
                pyautogui.press("space")
                self.multitask_btn = "mult"
        # elif "ctrl+alt+tab" == text:
        #     pyautogui.hotkey("ctrl", "alt", "tab")
        elif "alt+f4" == text:
            pyautogui.hotkey("alt", "f4")
        elif "ctrl+f4" == text:
            pyautogui.hotkey("ctrl", "f4")
        elif "ctrl+win+right" == text:
            pyautogui.hotkey("ctrl", "win", "right")
        elif "ctrl+win+left" == text:
            pyautogui.hotkey("ctrl", "win", "left")
        elif "hotkeys" == text:
            self.InlineButton_Hotkeys(update, content)
            # self.buttonfun(update, content)
        else:
            reply_controller = directory_controller.MainController(text)
            try:
                return_text = reply_controller.return_text
            except Exception as e:
                return_text = ""
            if return_text == 0:
                # update.message.reply_text("Sorry, I can't do that!") 
                print("Sorry, I can't do that!")
            elif len(return_text) > 1:
                # update.message.reply_text(return_text)
                print(return_text)
            else:
                pass
