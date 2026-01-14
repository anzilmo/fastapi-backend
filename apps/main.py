from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from apps.mongodb import users_collection
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/home")
def home():
    user = users_collection.find_one({}, {"_id": 0})
    return {
        "title": "FastAPI + React",
        "message": f"MongoDB connected for {user['name']}" if user else "MongoDB is empty"
    }

class UserIn(BaseModel):
    name: str

class UserOut(BaseModel):
    id: str
    name: str

@app.post("/user", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserIn):
    result = users_collection.insert_one({
        "name": user.name
    })

    return {
        "id": str(result.inserted_id),
        "name": user.name
    }