# -*- coding: utf-8 -*-
import sys
import os
import subprocess
import wx
import json
from threading import Thread
from sti import SystemTrayIcon
from sreader import SerialReader
from webserver import WebServer
from buttons import *


guiDir = os.path.join(os.getcwd(), "gui")
appThread = None
electronThread = None
serialThread = None
httpdThread = None
config = None

buttons = ["btn_0", "btn_1", "btn_2", "btn_3", "btn_4", "btn_5", "btn_6", "btn_7", "btn_8", "btn_9",
               "btn_a", "btn_b", "btn_c", "btn_d", "btn_e", "btn_f", "btn_g", "btn_h", "btn_i", "btn_j",
               "btn_k", "btn_l", "btn_m", "btn_n", "btn_o", "btn_p", "btn_q", "btn_r", "btn_s", "btn_t",
               "btn_u", "btn_v", "btn_w", "btn_x", "btn_y", "btn_z", "btn_?", "btn_!", "btn_/", "btn_&"]
specials = ["btn_@", "btn_#", "btn_+", "btn_-"]

def openGui():
    global electronThread
    electronThread = ElectronThread()
    electronThread.start()


def close():
    if appThread is not None:
        appThread.exit()
    if electronThread is not None:
        electronThread.exit()
    sys.exit()


def serial_command_parser(command):
    print(command)


class AppThread(Thread):
    app = None

    def run(self):
        self.app = wx.App(False)
        SystemTrayIcon(os.path.join(guiDir, "contents", "images", "icons", "icon.ico"), "BDeck", openGui, [
            ["Open", openGui],
            "separator",
            ["Exit", close]
        ])
        self.app.MainLoop()

    def exit(self):
        self.app.Destroy()

class ElectronThread(Thread):
    electron = None

    def run(self):
        self.electron = subprocess.run(["npm", "start"], cwd=guiDir, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def exit(self):
        subprocess.run(["taskkill", "/F", "/IM", "node.exe"], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

class Configuration:

    def __init__(self, file):
        self.file = file
        self.config = {"buttons": [], "macros": []}

    def exists(self):
        if os.path.isfile(self.file):
            return True
        else:
            return False

    def load(self):
        file = open(self.file, "r")
        self.config = self.decode(json.loads(file.read()))
        file.close()

    def save(self):
        file = open(self.file, "w")
        file.write(json.dumps(self.config, indent=4, cls=ButtonEncoder))
        file.close()

    def decode(self, dic):
        decoded = self.config
        for button in dic["buttons"]:
            btn = Button(button["button"], button["type"], None)

            if btn.type == "keyboard":
                action = Keyboard()

                for k in button["action"]["keys"]:
                    key = Key(k["key"], k["delay"], k["time"])
                    action.keys.append(key)

                btn.action = action
            elif btn.type == "command":
                btn.action = Command(button["action"]["command"])
            elif btn.type == "macro":
                btn.action = Macro(button["action"]["macro"])
            elif btn.type == "program":
                btn.action = Program(button["action"]["path"])
            elif btn.type == "internal":
                btn.action = Internal(button["action"]["command"])
            decoded["buttons"].append(btn)

        for macro in dic["macros"]:
            pass

        return decoded

    def get_button_from_name(self, name):
        for btn in self.config["buttons"]:
            if btn.button == name:
                return btn
        return None

    def get_button(self, index):
        if index.isdigit():
            return self.get_button_from_name(buttons[int(index) - 1])
        else:
            if index == "A":
                return self.get_button_from_name(specials[0])
            elif index == "B":
                return self.get_button_from_name(specials[1])
            elif index == "C":
                return self.get_button_from_name(specials[2])
            elif index == "D":
                return self.get_button_from_name(specials[3])
        return None


def main():
    global appThread
    global serialThread
    global httpdThread
    global config

    config = Configuration(os.path.join(os.getcwd(), "settings.json"))
    if not config.exists():
        config.save()
    config.load()

    appThread = AppThread()
    appThread.start()

    httpdThread = WebServer("localhost", 8080, config)
    httpdThread.start()

    serialThread = SerialReader("BDeck", serial_command_parser)
    serialThread.start()

    openGui()


if __name__ == "__main__":
    main()
