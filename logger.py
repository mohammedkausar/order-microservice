import json
import logging
import os
import sys
from datetime import datetime

SERVICE_NAME = "orders-service"
ENV = os.getenv("ENV", "dev")

class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname.lower(),
            "service": SERVICE_NAME,
            "env": ENV,
            "message": record.getMessage()
        }

        if isinstance(record.args, dict):
            log.update(record.args)

        return json.dumps(log)

def get_logger() -> logging.Logger:
    logger = logging.getLogger(SERVICE_NAME)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())

    logger.handlers.clear()
    logger.addHandler(handler)
    logger.propagate = False

    return logger

logger = get_logger()
