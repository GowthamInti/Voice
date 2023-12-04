from typing import Any, List, Literal, Optional, Union
import requests

from app.config import CONFIG
from pydantic import BaseModel
from app.models import load_pipeline
text2speech_example = {
    "model": "XTTS",
    "text": ("Hello, this is a test. I hope the TTS model can pronounce this correctly."),

    "speaker_wav_url":"http://65.21.65.49:8091/download/highpitch_fastspeed_highenergy.wav",
    "language":"en"
}

class _Text2Speech(BaseModel):
    model: str
    text: Union[str, List[str]]
    speaker_wav_url: Union[str, List[str]]
    language: Optional[str]= None
    class Config:
        arbitrary_types_allowed = True


class Text2SpeechQuery(_Text2Speech):

    class Config:
        schema_extra = {"example": text2speech_example}

    def to_inference_kwargs(self) -> dict:

        kwargs = self.dict(exclude_none=True) 
        url = kwargs['speaker_wav_url']
        kwargs['model'] = load_pipeline(kwargs['model'])
        save_path ="assets/audio1.wav"
        output_path ="assets/output.wav"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for any errors in the response

            with open(save_path, 'wb') as file:
                file.write(response.content)
            kwargs["speaker_wav"] = save_path
            kwargs.pop('speaker_wav_url')

        except requests.exceptions.RequestException as e:
            print(f"Download failed: {e}")

        kwargs["file_path"]=output_path
        # import ipdb;ipdb.set_trace()
        return kwargs
