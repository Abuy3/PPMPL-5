from fastapi import FastAPI, HTTPException
import random
import time

app = FastAPI()

# Simulasi database sederhana
users_db = {
    1: {"id": 1, "name": "User 1", "email": "user1@example.com"},
    2: {"id": 2, "name": "User 2", "email": "user2@example.com"},
    3: {"id": 3, "name": "User 3", "email": "user3@example.com"},
}

@app.get("/")
async def read_root():
    return {"message": "Welcome to Load Testing API"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    # Simulasi latency acak antara 100-500ms
    time.sleep(random.uniform(0.1, 0.5))
    
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@app.post("/users/")
async def create_user():
    # Simulasi latency yang lebih tinggi untuk operasi POST
    time.sleep(random.uniform(0.5, 1.0))
    
    new_id = max(users_db.keys()) + 1
    new_user = {
        "id": new_id,
        "name": f"User {new_id}",
        "email": f"user{new_id}@example.com"
    }
    users_db[new_id] = new_user
    return new_user

@app.get("/heavy")
async def heavy_operation():
    # Simulasi operasi berat
    time.sleep(random.uniform(1.0, 2.0))
    return {"status": "completed", "process": "heavy operation"}