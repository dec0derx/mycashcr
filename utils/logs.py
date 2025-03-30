import logging

# Configure logging
logging.basicConfig(
    filename='/var/log/flipmybucks/traffic.log',  # Log file path
    level=logging.INFO,               # Log level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
)