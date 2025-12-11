from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .middleware import RequestLoggerMiddleware

app = FastAPI()


# The frontend runs on a separate port, so we enable CORS
# to allow cross-origin requests to the API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_middleware(RequestLoggerMiddleware)


class SummaryRequest(BaseModel):
    text: str


class SummaryResponse(BaseModel):
    summary: str
    timestamp: str
    

@app.post("/summaries")
async def summaries(request: SummaryRequest) -> SummaryResponse:
    split_text = request.text.split(None, 10)
    res = split_text[:10]

    return SummaryResponse(
        summary=" ".join(res),
        timestamp=datetime.now(tz=timezone.utc).isoformat(),
    )


@app.get("/health")
async def root():
    return {"message": "OK"}
