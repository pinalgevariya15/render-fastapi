from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return{"message":"Hello from FastAPI on Render!"}
@app.get("/users")
def get_users():
    return {"users": ["Alice", "Bob", "Charlie"],
            "Role":["Admin", "Employee", "Guest"]}