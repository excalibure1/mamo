from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the MAMO Backend"}

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/api/status")
def api_status():
    return JSONResponse({"status": "ok", "service": "mamo-backend", "version": "0.1.0"})
