from fastapi import Request
from fastapi.responses import JSONResponse


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