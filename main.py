from fastapi import BackgroundTasks, FastAPI
from typing import Optional

from search_utils import find_dragon_files
from smsbomber import Bomber


app = FastAPI()

@app.get("/")
async def home():
    return {"status": "Welcome to API :)"}


@app.get("/bomb")
async def bomb(background_tasks: BackgroundTasks,number: str, noOfMsg: Optional[int] = 50):
    if len(number) == 10 and number.isdigit():
        pass
    else:
        return {"status": "Check Your Entries"}
    bombobj = Bomber(number, noOfMsg)
    background_tasks.add_task(bombobj.startBombing) # Calling it as background task so the responce dont take time.
    return {"status": "Sending"}


@app.get("/dragons")
async def dragon_files(root: Optional[str] = "."):
    """Search for files containing dragon-related keywords.

    The search covers both filenames and file contents looking for any of the
    following terms: "dragon", "dragon36", "3.6", and "3_6". Paths are
    returned relative to the provided ``root`` for easy reading.
    """

    matches = find_dragon_files(root or ".")
    return {"root": root or ".", "matches": matches}
