from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from app.utils import process_cv

app = FastAPI()

@app.post("/upload_cv/")
async def upload_cv(file: UploadFile = File(...)):
    content = await file.read()
    results = process_cv(content.decode('utf-8'))
    return JSONResponse(content=results)

