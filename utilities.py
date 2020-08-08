from pynput.keyboard import Key, KeyCode, Controller


def parse_key(key):
    if key == "Numpad0":
        return KeyCode.from_vk(96)
    elif key == "Numpad1":
        return KeyCode.from_vk(97)
    elif key == "Numpad2":
        return KeyCode.from_vk(98)
    elif key == "Numpad3":
        return KeyCode.from_vk(99)
    elif key == "Numpad4":
        return KeyCode.from_vk(100)
    elif key == "Numpad5":
        return KeyCode.from_vk(101)
    elif key == "Numpad6":
        return KeyCode.from_vk(102)
    elif key == "Numpad7":
        return KeyCode.from_vk(103)
    elif key == "Numpad8":
        return KeyCode.from_vk(104)
    elif key == "Numpad9":
        return KeyCode.from_vk(105)
    elif key == "Numpad/":
        return KeyCode.from_vk(111)
    elif key == "Numpad*":
        return KeyCode.from_vk(106)
    elif key == "Numpad-":
        return KeyCode.from_vk(109)
    elif key == "Numpad+":
        return KeyCode.from_vk(107)
    elif key == "Tab":
        return Key.tab
    elif key == "Shift":
        return Key.shift
    elif key == "Ctrl_L":
        return Key.ctrl_l
    elif key == "Win" or key == "Cmd":
        return Key.cmd
    elif key == "Alt_L":
        return Key.alt_l
    elif key == "Space":
        return Key.space
    elif key == "AltGr":
        return Key.alt_gr
    elif key == "Menu":
        return Key.menu
    elif key == "Ctrl_R":
        return Key.ctrl_r
    elif key == "Backspace":
        return Key.backspace
    elif key == "Del":
        return Key.delete
    elif key == "Home":
        return Key.home
    elif key == "End":
        return Key.end
    elif key == "Page_Up":
        return Key.page_up
    elif key == "Page_Down":
        return Key.page_down
    elif key == "NumLock":
        return Key.num_lock
    elif key == "Enter":
        return Key.enter
    elif key == "Up":
        return Key.up
    elif key == "Left":
        return Key.left
    elif key == "Down":
        return Key.down
    elif key == "Right":
        return Key.right
    elif key == "Esc":
        return Key.esc
    elif key == "F1":
        return Key.f1
    elif key == "F2":
        return Key.f2
    elif key == "F3":
        return Key.f3
    elif key == "F4":
        return Key.f4
    elif key == "F5":
        return Key.f5
    elif key == "F6":
        return Key.f6
    elif key == "F7":
        return Key.f7
    elif key == "F8":
        return Key.f8
    elif key == "F9":
        return Key.f9
    elif key == "F10":
        return Key.f10
    elif key == "F11":
        return Key.f11
    elif key == "F12":
        return Key.f12
    elif key == "MediaPlayPause":
        return Key.media_play_pause
    elif key == "MediaNext":
        return Key.media_next
    elif key == "MediaPrevious":
        return Key.media_previous
    elif key == "MediaVolumeUp":
        return Key.media_volume_up
    elif key == "MediaVolumeDown":
        return Key.media_volume_down
    elif key == "MediaVolumeMute":
        return Key.media_volume_mute
    else:
        if len(key) == 1:
            return KeyCode.from_char(char=char(key))
        else:
            return key
