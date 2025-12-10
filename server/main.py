from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .middleware import RequestLoggerMiddleware

app = FastAPI()

app.add_middleware(RequestLoggerMiddleware)

# To support frontend adding cors.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SummaryRequest(BaseModel):
    text: str


@app.post("/summaries")
async def summaries(request: SummaryRequest):
    result = request.text.split(None, 10)

    return {
        "summary": " ".join(result[:10]),
        "timestamp": datetime.now(tz=timezone.utc).isoformat(),
    }


@app.get("/health")
async def root():
    return {"message": "OK"}
