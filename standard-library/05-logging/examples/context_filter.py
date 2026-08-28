import contextvars
import logging
import sys


request_id_var = contextvars.ContextVar("request_id", default="-")


class RequestContextFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = request_id_var.get()
        return True


logger = logging.getLogger("study.context")
logger.setLevel(logging.INFO)
logger.propagate = False

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(
    logging.Formatter("%(levelname)s:%(request_id)s:%(message)s")
)
handler.addFilter(RequestContextFilter())
logger.addHandler(handler)

request_id_var.set("req-104")
logger.info("request started")
