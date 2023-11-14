import subprocess
from typing import List

from fire import Fire

base_cmd = ["python", "-m", "app.main"]


def text2speech(
    pipeline__name: str = "tts_models/multilingual/multi-dataset/xtts_v2",
    pipeline__pipeline: str = "TTS",
    
):
    cmd = [
        f'pipeline__name="{pipeline__name}"',
        f"pipeline__pipeline={pipeline__pipeline}",
        "DEBUG=true",
    ] + base_cmd
    subprocess.run(" ".join(cmd), shell=True)

if __name__ == "__main__":
    Fire(
        {
            "text2speech": text2speech,
        }
    )