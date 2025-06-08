Keylogger
A simple keylogger built with Python and pynput to log keystrokes with timestamps, key combinations, encryption, and system tray support.


Setup:
Create a virtual environment:python -m venv venv
Activate the virtual environment:
Windows: venv\Scripts\activate
Install dependencies:pip install -r requirements.txt
Run the keylogger:python main.py


Configuration:
Edit config.json to customize:
log_file: Path to the log file (default: logs/keylog.txt).
key_mappings: Map special keys to their output (e.g., "space": " ").


Output:
Logs are encrypted and written to the file specified in config.json. Example decrypted output:
[06/07/25 10:05:23 PM] H
[06/07/25 10:05:24 PM] [SPACE]
[06/07/25 10:05:25 PM] Ctrl+C
[06/07/25 10:05:26 PM] Shift+[F1]

Logs rotate daily, with up to 7 days of backups (e.g., logs/keylog.txt.2025-06-07).
Use scripts/decrypt_logs.py to view logs:python scripts/decrypt_logs.py logs/keylog.txt


System Tray:
The keylogger runs in the background with a system tray icon.
Right-click the icon and select "Exit" to stop the keylogger.


Notes:
Ensure you have write permissions for the logs/ directory.
The key.key file stores the encryption key; keep it secure and do not share it.
The pykey/ directory contains the core modules (config.py, logger.py).
Use responsibly and with consent, as keyloggers can capture sensitive data.