import logging
import torch
from TTS.api import TTS 
from fastapi.exceptions import HTTPException
from fastapi import status

from app.config import PipelineConfig
from app.utils import CUDA_IS_AVAILABLE,DEVICE
from app.exceptions import (
    UnsupportedException,
    UnsupportedModelException,
    UnsupportedPipelineException,
    UnsupportedSchedulerException,
)

SUPPORTED_MODELS = ['tts_models/multilingual/multi-dataset/xtts_v2', 
                    'tts_models/multilingual/multi-dataset/your_tts', 
                    'tts_models/multilingual/multi-dataset/bark',
                    'tts_models/en/vctk/vits',
                    'tts_models/en/vctk/fast_pitch'
                    ]

def load_tts_pipeline(
    name: str,
    pipeline_name: str,
):
    if name not in SUPPORTED_MODELS:
        msg = (
            f"Model: {name}, is not supported."
            f"\nPlease choose from one of {[k for k in SUPPORTED_MODELS]}"
        )
        logger.exception(msg)
        raise UnsupportedModelException(msg)

    tts = TTS(name).to(DEVICE)
    return tts
    

def load_pipeline(config: PipelineConfig):
    try:
        pipe = load_tts_pipeline(
                name=config.name,
                pipeline_name=config.pipeline,
        )
    except UnsupportedException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.args)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.args
        )
    return pipe