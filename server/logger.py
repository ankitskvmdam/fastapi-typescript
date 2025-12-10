import logging

logging.basicConfig(
    level=logging.INFO,
    format="\033[35m\033[1m\033[47m [Logger] %(asctime)s \033[0m %(message)s\033[0m",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)
