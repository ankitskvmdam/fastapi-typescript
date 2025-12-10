import time

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from .logger import logger


class RequestLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        start_time = time.perf_counter()
        try:
            response = await call_next(request)
        except Exception as e:
            logger.exception(f"Error occurred while processing request: {e}")
            raise e
        execution_time = time.perf_counter() - start_time
        logger.info(
            {
                "request_path": request.url.path,
                "execution_time": execution_time,
                "status_code": response.status_code,
            }
        )

        return response
