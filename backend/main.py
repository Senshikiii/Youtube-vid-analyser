from fastapi import FastAPI
from pydantic import BaseModel
from transcript import get_transcript
from analyzer import analyze


app = FastAPI()

class VideoRequest(BaseModel):
    url: str

@app.post("/analyze")
async def analyze_video(request: VideoRequest):
    url = request.url
    transcript = get_transcript(url)
    result = analyze(transcript)
    return result


