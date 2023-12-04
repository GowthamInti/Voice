import logging
import torch
from TTS.api import TTS 
from fastapi.exceptions import HTTPException
from fastapi import status

from app.utils import CUDA_IS_AVAILABLE,DEVICE
from app.exceptions import (
    UnsupportedException,
    UnsupportedModelException,
    UnsupportedPipelineException,
    UnsupportedSchedulerException,
)

SUPPORTED_MODELS = {'XTTS':'tts_models/multilingual/multi-dataset/xtts_v2',
                    'XTTS_fastpitch': 'tts_models/en/ljspeech/fast_pitch',
                    }


def load_tts_pipeline(name):

    if name not in SUPPORTED_MODELS:
        msg = (
            f"Model: {name}, is not supported."
            f"\nPlease choose from one of {[k for k in SUPPORTED_MODELS]}"
        )
        logger.exception(msg)
        raise UnsupportedModelException(msg)
    if name == "XTTS":
        model = TTS( SUPPORTED_MODELS[name], progress_bar=False).to(DEVICE)
    if name == "XTTS_fastpitch":
        model = TTS( SUPPORTED_MODELS[name], progress_bar=False).to(DEVICE)
    return model

def load_pipeline(model_name):
    try: 

        pipe = load_tts_pipeline(model_name)
    except UnsupportedException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.args)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.args
        )
    return pipe