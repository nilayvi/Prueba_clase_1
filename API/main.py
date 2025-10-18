from fastapi import FastAPI
app = FastAPI()
@app.get("/files")
def getfiles():
    pass

@app.post("/files")
def postfiles():
    pass

@app.get("/files/{file_name}")
def getfile(file_name: str):
    pass
    