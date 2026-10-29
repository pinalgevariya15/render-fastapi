from fastapi import FastAPI
app = FastAPI()

image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0alz_4QfS7tx0wsk8YEeV9r2G4XYdX-ys1p4z7IXC4A&s=10"

@app.get("/")
def home():
    return{"message":"Hello from FastAPI on Render!"}
@app.get("/users")
def get_users():
    return {"users": ["Alice", "Bob", "Charlie"],
            "Role":["Admin", "Employee", "Guest"]}

@app.get("/image")
def get_image():
    return{"image_url": image}