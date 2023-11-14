
import logging
from contextlib import asynccontextmanager
import uvicorn
from app.config import CONFIG
from app.models import load_pipeline
from app.schemas import (
    Text2SpeechQuery,
)
from app.utils import wavfile
from fastapi import FastAPI
from fastapi.responses import Response,FileResponse
from fastapi.middleware.cors import CORSMiddleware


logger = logging.getLogger(__file__)


logger.info("App opened")
SUPPORTED_PIPELINES = [
    "TTS",
]


if CONFIG.pipeline.pipeline not in SUPPORTED_PIPELINES:
    e = CONFIG.pipeline.pipeline
    raise ValueError((f"Endpoint: {e}. Is not one of: {SUPPORTED_PIPELINES}"))


pipeline = []

@asynccontextmanager
async def lifespan(app: FastAPI):
    if CONFIG.pipeline.pipeline == "TTS":
        logger.info("loading training params")
        pipeline.append(load_pipeline(CONFIG.pipeline))
    yield
    pipeline[0].to("cpu")


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/text2speech",response_class=FileResponse(str, media_type="audio/wav"))
async def text2speech(q: Text2SpeechQuery):
    data_dict = q.to_inference_kwargs()
    pipeline[0].tts_to_file(**data_dict)
    return FileResponse(data_dict['file_path'], media_type="audio/wav")


@app.get(CONFIG.AIP_HEALTH_ROUTE, status_code=200)
async def health():
    return {"status": 200}



if __name__ == "__main__":
    
    print(CONFIG.json(indent=2))
    uvicorn.run(
        "app.main:app", host="0.0.0.0", port=CONFIG.AIP_HTTP_PORT, reload=CONFIG.DEBUG
    )