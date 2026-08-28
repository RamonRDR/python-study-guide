import logging


class RecordCollector(logging.Handler):
    def __init__(self) -> None:
        super().__init__()
        self.records: list[logging.LogRecord] = []

    def emit(self, record: logging.LogRecord) -> None:
        self.records.append(record)


logger = logging.getLogger("study.stacklevel")
logger.setLevel(logging.INFO)
logger.propagate = False
collector = RecordCollector()
logger.addHandler(collector)


def log_notice(message: str) -> None:
    logger.info(message, stacklevel=2)


def run_job() -> None:
    log_notice("job started")


run_job()
record = collector.records[0]
print(f"{record.levelname}:{record.funcName}:{record.getMessage()}")
