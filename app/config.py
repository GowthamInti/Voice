from typing import List, Optional

from pydantic import BaseModel, BaseSettings

class PipelineConfig(BaseModel):
    name: str = "tts_models/en/vctk/vits"
    pipeline: str = "TTS"

class Config(BaseSettings):
    pipeline: PipelineConfig = PipelineConfig()
    AIP_HEALTH_ROUTE: str = "/health"
    AIP_HTTP_PORT: int = 8000
    DEBUG: bool = False
    HF_HUB_OFFLINE: bool = True
    AIP_ENDPOINT_ID: str = ""
    AIP_DEPLOYED_MODEL_ID: str = ""
    AIP_STORAGE_URI: str = ""

    class Config:
        env_nested_delimiter = "__"


try:
    # Hack for running locally
    from dotenv import load_dotenv

    load_dotenv()
except:
    pass


CONFIG = Config()