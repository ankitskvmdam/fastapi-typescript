from datetime import datetime, timezone

from fastapi import FastAPI
from middleware import RequestLoggerMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(RequestLoggerMiddleware)


class SummariesRequest(BaseModel):
    """Summaries request."""

    text: str


@app.post("/summaries")
async def summaries(request: SummariesRequest):
    result = request.text.split(None, 10)

    return {
        "summary": " ".join(result[:10]),
        "timestamp": datetime.now(tz=timezone.utc),
    }


@app.get("/health")
async def root():
    return {"message": "OK"}
