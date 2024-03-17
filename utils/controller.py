import os, pyautogui
import directory_controller



class PcController():
    # change to home directory
    directory_controller.cd_home_location()

    def __init__(self):
        self.multitask_btn = "mult"

    # def InlineButton(self, update, content):
    #     button_text = [["Pause", "Play"], ["Volume Down", "Mute","Volume Up"], ["Back Forward", "Fast Forward"], "Fullscreen", "Quit", ["Shutdown", "Cancel Shutdown"]]

    # def InlineButton_Hotkeys(self, update, content):
    #     button_text = [["⬅️", "Multitask", "➡️"], "Switch Tabs", ["Previous Workpace", "Next Workspace"], "Close Tab", "Close Window"]
    #     button_reply = [["back forward", "multitask", "fast forward"], "ctrl+tab", ["ctrl+win+left", "ctrl+win+right"], "ctrl+f4", "alt+f4"]

    def shut_down(self, time1=20):
        cont = "shutdown -s -t %s" % time1
        os.system(cont)
        ans = "Your PC will be turned off within 20 Seconds, 'Stop Shutdown' to Stop the shutdown"
        return ans


    def call(self, text):
        self.text = text
        self.command_center()

    def hotkey_call(self, text):
        text = text.split("_")
        text.pop()
        text = tuple(text)
        # print(text)
        pyautogui.hotkey(*text)

    def press(self, text):
        text = text[:text.find("_press")]
        pyautogui.press(text)

    def get_return_value(self):
        if (len(self.return_text) > 0):
            return self.return_text
        else:
            return "None"

    def command_center(self):
        text = self.text

        if "stop shutdown" == text:
            self.CancelShutDown()
        elif ("shutdown") in text:
            # text = str(update.message.text).lower()
            sts = self.shut_down()
            # update.message.reply_text(sts)
        elif "quit" == text:
            quit()

        elif "volume" in text:
            if "up" in text:
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
            elif "down" in text:
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')

            else:
                pass
        elif ("press" in text):
            self.press(text)
        elif ("hotkey" in text):
            self.hotkey_call(text)

        elif "mute" == text:
            pyautogui.press("volumemute")
        elif ("maximize" and "window") in text:
            MaxWindow()

        elif "multitask" == text:
            if self.multitask_btn == "mult":
                pyautogui.hotkey("ctrl", "alt", "tab")
                self.multitask_btn = "selt"
            else:
                pyautogui.press("space")
                self.multitask_btn = "mult"
        # elif "ctrl+alt+tab" == text:
        #     pyautogui.hotkey("ctrl", "alt", "tab")
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
                # print(return_text)
                self.return_text = return_text
            else:
                pass