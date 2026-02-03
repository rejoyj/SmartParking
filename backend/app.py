from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

STATUS_FILE = "parking_status.json"

# create default parking file
if not os.path.exists(STATUS_FILE):
    with open(STATUS_FILE, "w") as f:
        json.dump({
            "Slot 1": False,
            "Slot 2": False,
            "Slot 3": False
        }, f)

@app.get("/")
def home():
    return {"message": "Smart Parking Backend Running"}

@app.get("/status")
def get_status():
    with open(STATUS_FILE) as f:
        return json.load(f)

@app.post("/update")
def update_status(data: dict):
    with open(STATUS_FILE, "w") as f:
        json.dump(data, f)
    return {"success": True}
