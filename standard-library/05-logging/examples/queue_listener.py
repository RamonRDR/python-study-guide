import logging
import queue
import sys
from logging.handlers import QueueHandler, QueueListener


log_queue = queue.Queue()
output_handler = logging.StreamHandler(sys.stdout)
output_handler.setFormatter(
    logging.Formatter("%(levelname)s:%(name)s:%(message)s")
)

logger = logging.getLogger("study.queue")
logger.setLevel(logging.INFO)
logger.propagate = False
logger.addHandler(QueueHandler(log_queue))

listener = QueueListener(
    log_queue,
    output_handler,
    respect_handler_level=True,
)
listener.start()
try:
    logger.info("queued event")
finally:
    listener.stop()
