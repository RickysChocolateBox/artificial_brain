import argparse
import logging
import configparser
import sys
from temperature_sensor_app import SensorApp

def parse_arguments():
    parser = argparse.ArgumentParser(description="Temperature Sensor Application")
    parser.add_argument("--config", dest="config_file", help="Path to the configuration file", default="temperature_sensor_config.ini")
    return parser.parse_args()

def read_configuration(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

def configure_logging(config):
    log_file = config.get("Logging", "log_file", fallback=None)
    debug = config.getboolean("Logging", "debug", fallback=False)
    log_level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(filename=log_file, level=log_level, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    args = parse_arguments()
    config = read_configuration(args.config_file)
    configure_logging(config)

    try:
        logging.info("Starting the application")
        app = SensorApp()
        app.mainloop()
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        sys.exit(1)

    logging.info("Application terminated successfully")

if __name__ == "__main__":
    main()
