from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List
from pathlib import Path
import os   

app = FastAPI()

        
# Configuration: directory to store files. Use a directory named 'files' relative to repo root.
DEFAULT_DIR = Path(__file__).parent.parent / "files"
FILE_DIR = DEFAULT_DIR.resolve()


class FileCreate(BaseModel):
    filename: str = Field(..., min_length=1)
    content: str = Field(...)


def _secure_filename(name: str) -> str:
    """Basic filename validation to prevent path traversal.

    - Disallow path separators and parent-up segments.
    - Return the base name.
    """
    if ".." in name or "/" in name or "\\" in name:
        raise ValueError("invalid filename")
    # Also strip any leading/trailing whitespace
    cleaned = name.strip()
    if cleaned == "":
        raise ValueError("empty filename")
    return os.path.basename(cleaned)


@app.on_event("startup")
def _ensure_dir_exists():
    try:
        FILE_DIR.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        # If directory cannot be created, raise on startup so errors are visible.
        raise RuntimeError(f"could not create file directory: {e}")


@app.get("/files", response_model=dict)
def getfiles() -> dict:
    """Return a JSON object with a list of filenames in the configured directory.

    Response: { "files": ["a.txt", "b.txt"] }
    """
    try:
        files = [p.name for p in FILE_DIR.iterdir() if p.is_file()]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    return {"files": files}


@app.post("/files", status_code=status.HTTP_201_CREATED, response_model=dict)
def postfiles(payload: FileCreate) -> dict:
    """Create or overwrite a file in the configured directory.

    Expects JSON body: { "filename": "example.txt", "content": "..." }
    Returns: { "message": "created", "filename": "example.txt" }
    """
    try:
        fname = _secure_filename(payload.filename)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid filename")

    dest = FILE_DIR / fname
    try:
        # Write using utf-8 encoding
        dest.write_text(payload.content, encoding="utf-8")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return {"message": "created", "filename": fname}


@app.get("/files/{file_name}", response_model=dict)
def getfile(file_name: str) -> dict:
    try:
        fname = _secure_filename(file_name)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid filename")

    target = FILE_DIR / fname
    if not target.exists() or not target.is_file():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="file not found")

    try:
        content = target.read_text(encoding="utf-8")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return {"filename": fname, "content": content}
    