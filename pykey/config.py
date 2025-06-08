import json

def load_config(config_file="config.json"):
    try:
        with open(config_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {config_file} not found. Using default settings.")
        return {
            "log_file": "logs/keylog.txt",
            "key_mappings": {
                "space": " ",
                "enter": "\n",
                "tab": "\t",
                "backspace": "[BACKSPACE]",
                "shift": "[SHIFT]",
                "ctrl_l": "[CTRL]",
                "alt_l": "[ALT]",
                "esc": "[ESC]",
                "up": "[UP]",
                "down": "[DOWN]",
                "left": "[LEFT]",
                "right": "[RIGHT]",
                "f1": "[F1]",
                "f2": "[F2]",
                "f3": "[F3]",
                "f4": "[F4]",
                "delete": "[DELETE]",
                "home": "[HOME]",
                "end": "[END]",
                "page_up": "[PGUP]",
                "page_down": "[PGDN]",
                "caps_lock": "[CAPS]"
            }
        }
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {config_file}. Using default settings.")
        return {
            "log_file": "logs/keylog.txt",
            "key_mappings": {
                "space": " ",
                "enter": "\n",
                "tab": "\t",
                "backspace": "[BACKSPACE]",
                "shift": "[SHIFT]",
                "ctrl_l": "[CTRL]",
                "alt_l": "[ALT]",
                "esc": "[ESC]",
                "up": "[UP]",
                "down": "[DOWN]",
                "left": "[LEFT]",
                "right": "[RIGHT]",
                "f1": "[F1]",
                "f2": "[F2]",
                "f3": "[F3]",
                "f4": "[F4]",
                "delete": "[DELETE]",
                "home": "[HOME]",
                "end": "[END]",
                "page_up": "[PGUP]",
                "page_down": "[PGDN]",
                "caps_lock": "[CAPS]"
            }
        }