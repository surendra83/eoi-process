import time
import uuid
import json
from core.logger import app_logger
from starlette.middleware.base import BaseHTTPMiddleware


async def _replay_body(request, body: bytes):
    # downstream handlers must still be able to read the body after middleware consumes it
    async def receive():
        return {"type": "http.request", "body": body}
    request._receive = receive


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request_id =f"eoi-{uuid.uuid4().hex[:8]}"
        start = time.perf_counter()

        body_bytes = await request.body()
        await _replay_body(request, body_bytes)
        try:
            request_body = json.loads(body_bytes) if body_bytes else None
        except json.JSONDecodeError:
            request_body = None

        with app_logger.contextualize(
            log_type="APPLICATION",
            request_id=request_id,
            client_ip=request.client.host if request.client else "unknown",
            user_agent=request.headers.get("user-agent"),
            endpoint=request.url.path,
            request_method=request.method,
            request_body=request_body,
            execute_method="dispatch"
        ):
            response = await call_next(request)
            response_time_ms = round((time.perf_counter() - start) * 1000, 2)
            app_logger.bind(response_time_ms=response_time_ms).info(
                f"{request.method} {request.url.path.strip('/').split('/')[-1].capitalize()} request completed"
                )

        response.headers["X-Request-ID"] = request_id
        return response