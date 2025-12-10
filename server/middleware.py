import time

from logger import logger
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response


class RequestLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        start_time = time.perf_counter()
        response = await call_next(request)
        execution_time = time.perf_counter() - start_time
        logger.info(
            {
                "request_path": request.url.path,
                "execution_time": execution_time,
                "status_code": response.status_code,
            }
        )

        return response
