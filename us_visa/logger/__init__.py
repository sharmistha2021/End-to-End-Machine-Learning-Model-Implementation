import logging
import os
from datetime import datetime
from us_visa.utils.from_root import from_root  # updated import

# Create a timestamped log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir = 'logs'

# Full path to the log file at the project root
logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

# Ensure the logs directory exists
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

# Configure logging to file
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

# Optional: also log to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
logging.getLogger('').addHandler(console_handler)

# Test logging
logging.info("Logger is set up and ready!")
logging.debug("Debug message")
logging.warning("Warning message")
logging.error("Error message")
