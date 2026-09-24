from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


class APIException(Exception):
    def __init__(self, status_code: int, messages: str):
        self.status_code = status_code
        self.messages = messages


async def api_exception_handler(request: Request, exc: APIException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status_code": exc.status_code,
            "messages": exc.messages,
        },
    )

async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        if error["type"] == "json_invalid":
            errors.append({
                "field": "request",
                "message": "Invalid request",
            })
            continue

        field = ".".join(
            str(location)
            for location in error["loc"]
            if location != "body"
        )

        message = error["msg"]
        if error["type"] == "string_pattern_mismatch":
            message = f"{field} must contain only numeric digits"

        errors.append({
            "field": field,
            "message": message,
        })

    return JSONResponse(
        status_code=422,
        content={
            "status_code": 422,
            "errors": errors,
        },
    )