from loguru import logger
import sys
import json

logger.remove()

logger.add(
    "logs/eoi.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO"
)

# logger.add(
#     sys.stdout,
#     level="INFO",
#     serialize=True
# )

logger.add(
    "logs/application.log",
    level="INFO",
    rotation="100 MB",
    retention="90 days",
    compression="zip",
    serialize=True
)

logger.add(
    "logs/audit.log",
    level="INFO",
    rotation="100 MB",
    retention="7 years",
    compression="zip",
    serialize=True,
    filter=lambda record: record["extra"].get("log_type") == "AUDIT"
)

logger.add(
    "logs/error.log",
    level="ERROR",
    rotation="50 MB",
    retention="365 days",
    backtrace=True,
    diagnose=True,
    serialize=True
)

app_logger = logger
