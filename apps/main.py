from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.mongodb import users_collection



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[" http://localhost:5173/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/home")
def home():
        return {
        "title": "Welcome to the FastAPI Application",
        "description": "This is a sample FastAPI application with CORS enabled.",
    }


@app.get("/")
def read_root():
    user = users_collection.find_one({}, {"_id": 0})
    return {"user": user}
