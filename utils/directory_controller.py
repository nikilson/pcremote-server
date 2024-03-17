import time
import pyautogui
from win32api import GetLogicalDriveStrings
import webbrowser as web
from utils.whatkit import playonyt
from os import path
import os


class MainController():

    def __init__(self, text):
        self.text = text
        # self.find_home_loc()
        self.return_text = ""
        self.current_location = os.getcwd()
        self.drives = GetLogicalDriveStrings()
        self.drives = self.drives.split('\000')[:-1]
        # os.chdir(self.home_location)
        self.command_reader()

    def command_reader(self):

        if self.text == "pwd":
            self.print_working_directory()
        elif self.text[:3] == "cd ":
            self.text = self.text.replace("cd ", "")
            self.change_directory()
        elif self.text[:5] == "open ":
            self.text = self.text.replace("open ", "")
            self.open_file()
        elif ("ls" == self.text) or ("dir" == self.text):
            self.list_working_directory()
        else:
            self.return_text = 0

    def change_directory(self):
        dir_list = os.listdir(self.current_location)
        for n, txt in enumerate(dir_list):
            if self.text == txt.lower():
                self.text = txt
            elif self.text == str(n):
                self.text = txt
            else:
                pass
        tmp_location = path.join(self.current_location, self.text)
        tmp_location = path.realpath(tmp_location)

        if path.isdir(tmp_location):
            self.current_location = tmp_location
            os.chdir(self.current_location)
        elif path.isfile(tmp_location):
            self.return_text = f"{self.text} is a file!!"
        else:
            self.return_text = "Invalid location!!"
            # print("Invaild")

        # print(self.home_location)

    def print_working_directory(self):
        self.return_text = self.current_location

    def list_working_directory(self):
        print(self.current_location)
        dir_list = os.listdir(self.current_location)
        if self.current_location in self.drives:
            dir_list += self.drives

        for n, txt in enumerate(dir_list):
            if (n == 0):
                self.return_text += f"{txt}"
            else:
                self.return_text += f"/{txt}"

    def open_file(self):
        dir_list = os.listdir(self.current_location)
        for n, txt in enumerate(dir_list):
            if self.text == txt.lower():
                self.text = txt
            elif self.text == str(n):
                self.text = txt
            else:
                pass
        tmp_location = path.join(self.current_location, self.text)
        tmp_location = path.realpath(tmp_location)
        if path.isdir(tmp_location):
            # self.return_text = f"{self.text} is a directory!!"
            self.change_directory()
            # os.chdir(self.current_location)
        elif path.isfile(tmp_location):
            os.startfile(tmp_location)
        else:
            self.return_text = "Invaild file!!"


def cd_home_location(current_location):
    home_location = path.expanduser('~')
    if current_location and path.isdir(current_location):
        os.chdir(current_location)
    else:
        os.chdir(home_location)
        current_location = home_location
    return f"Current directory has been changed to {current_location}"


def list_working_directory(current_location):
    dir_list = os.listdir(current_location)
    drives = GetLogicalDriveStrings().split('\000')[:-1]
    if current_location in drives:
        dir_list += drives
    return dir_list


def get_current_directory():
    return os.getcwd()


def YTvideo(song):
    song = (song.lower()).replace("play", "")
    link = playonyt(song)
    web.open(link)
    time.sleep(10)
    # print("hi")
    pyautogui.press("f")


if __name__ == '__main__':
    MainController("cd ../../../../Documents/mydir")
    # YTvideo("play tech with tim")
