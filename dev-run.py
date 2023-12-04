import subprocess
from typing import List

from fire import Fire

base_cmd = ["python", "-m", "app.main"]


def text2speech():
    cmd = [
        "DEBUG=true",
    ] + base_cmd
    subprocess.run(" ".join(cmd), shell=True)

if __name__ == "__main__":
    Fire(
        {
            "text2speech": text2speech,
        }
    )