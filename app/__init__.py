from core import toxicity_of
from fastapi import FastAPI, Body
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/", include_in_schema=False)
async def read_root():
    return RedirectResponse("/docs")


@app.post("/sentiment/toxicity")
async def analyze_message(req=Body()):
    # curl http://localhost:8000/sentiment/toxicity  -H 'Content-Type: application/json' -d '{"message":"####fuck you"}'
    msg = req["message"]
    return {"source": msg, "toxicity": float(toxicity_of(msg))}
