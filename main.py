from pykey.config import load_config
from pykey.logger import start_logger

def main():
    # Load configuration
    config = load_config()
    
    # Start logger
    start_logger(config["log_file"], config["key_mappings"])

if __name__ == "__main__":
    main()