from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.utils import process_cv
import os
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

# Ensure the API key is loaded correctly
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

app = FastAPI()

@app.post("/upload_cv/")
async def upload_cv(file: UploadFile = File(...)):
    try:
        content = await file.read()
        results = process_cv(content, file.content_type)
        # Format the JSON response for readability
        formatted_results = json.dumps(results, indent=4)
        return JSONResponse(content=json.loads(formatted_results))
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="The uploaded file must be a text or PDF file.")
    except Exception as e:
        # Log the error
        print(f"Error: {e}")
        # Return a 500 Internal Server Error with a detailed message
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
 
