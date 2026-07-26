from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = ROOT / "logs"
LOG_FILE = LOG_DIR / "install.log"


class Logger:

    @staticmethod
    def initialize():
        LOG_DIR.mkdir(exist_ok=True)

    @staticmethod
    def write(message):
        Logger.initialize()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(LOG_FILE, "a") as log:
            log.write(f"[{timestamp}] {message}\n")

        print(message)
