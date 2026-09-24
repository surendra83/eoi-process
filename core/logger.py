import sys
import json
import uuid
from loguru import logger
from core.config import settings
logger.remove()

def _build_json_record(record):
    extra = record["extra"]
    payload = {
        "timestamp": record["time"].strftime("%Y-%m-%dT%H:%M:%SZ"),
        "log_type": extra.get("log_type", "APPLICATION"),
        "log_id": extra.get("log_id", str(uuid.uuid4())),
        "request_id": extra.get("request_id", str(uuid.uuid4())[:8]),
        "client_ip": extra.get("client_ip"),
        "user_agent": extra.get("user_agent"),
        "request_method": extra.get("request_method"),
        "endpoint": extra.get("endpoint"),
        "response_time_ms": extra.get("response_time_ms"),
        "request_body": extra.get("request_body"),
        "execute_method": extra.get("execute_method", record["function"]),
        "message": record["message"],
    }
    record["extra"]["serialized"] = json.dumps(payload, default=str)


logger = logger.patch(_build_json_record)
_JSON_FORMAT = "{extra[serialized]}\n"

# logger.add(
#     sys.stdout,
#     level=settings.LOG_LEVEL,
#     format=_JSON_FORMAT,
#     enqueue=True,
# )

logger.add(
    "logs/application.log",
    level=settings.LOG_LEVEL,
    format=_JSON_FORMAT,
    rotation="100 MB",
    retention="90 days",
    compression="zip",
    enqueue=True,
)

logger.add(
    "logs/audit.log",
    level="INFO",
    format=_JSON_FORMAT,
    rotation="100 MB",
    retention="7 years",
    compression="zip",
    enqueue=True,
    filter=lambda record: record["extra"].get("log_type") == "AUDIT",
)
logger.add(
    "logs/error.log",
    level="ERROR",
    format=_JSON_FORMAT,
    rotation="50 MB",
    retention="365 days",
    backtrace=True,
    diagnose=settings.ENV != "production",  # never leak locals/vars in prod
    enqueue=True,
)

app_logger = logger