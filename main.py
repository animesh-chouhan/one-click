from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import redis

app = FastAPI()

# Connect to Redis
r = redis.Redis(host="localhost", port=6379, db=0)

# Serve static files from public/ (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="public"), name="static")


@app.get("/")
def serve_index():
    return FileResponse("public/index.html")


@app.post("/click")
def click():
    new_val = r.incr("click_count")
    return {"count": new_val}


@app.get("/count")
def get_count():
    val = r.get("click_count")
    return {"count": int(val) if val else 0}
