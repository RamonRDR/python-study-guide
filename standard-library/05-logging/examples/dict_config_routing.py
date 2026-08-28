import logging
import logging.config
import sys


config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "brief": {
            "format": "%(levelname)s:%(name)s:%(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "brief",
            "level": "INFO",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        "study.service": {
            "level": "INFO",
            "propagate": True,
        }
    },
    "root": {
        "level": "WARNING",
        "handlers": ["console"],
    },
}

logging.config.dictConfig(config)

service_logger = logging.getLogger("study.service")
dependency_logger = logging.getLogger("study.dependency")

service_logger.info("service started")
dependency_logger.info("hidden detail")
dependency_logger.warning("slow response")
