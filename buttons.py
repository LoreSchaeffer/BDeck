from json import JSONEncoder

class Button:

    def __init__(self, button, t, action):
        self.button = button
        self.type = t
        self.action = action


class Keyboard:

    def __init__(self, keys=None):
        if keys is None:
            keys = []
        self.keys = keys

    def add_key(self, key):
        self.keys.append(key)

    def remove_key(self, key):
        for k in self.keys:
            if k.key == key.key:
                self.keys.remove(k)
                return


class Key:

    def __init__(self, key, delay, time):
        self.key = key
        self.delay = delay
        self.time = time


class Command:

    def __init__(self, command):
        self.command = command


class Macro:

    def __init__(self, macro):
        self.macro = macro


class Program:

    def __init__(self, path):
        self.path = path


class Internal:

    def __init__(self, command):
        self.command = command


class ButtonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
