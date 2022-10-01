from core import toxicity_of
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/", include_in_schema=False)
async def read_root():
    return RedirectResponse("/docs")


@app.get("/sentiment/toxicity")
async def analyze_message(q: str = Query(default="")):
    if q == "":
        raise HTTPException(
            status_code=400,
            detail="pass the message in as a query string: ?q=message")
    return {"toxicity": float(toxicity_of(q))}
