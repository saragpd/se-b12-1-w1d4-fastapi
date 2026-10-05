import fastapi 
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def read_root():
    return {"Welcome to Social Eagle Community"}

@app.get("/welcome/{name}")
def wel_user(name: str):
    return {"message": f"Welcome to Social Eagle Community, {name}!"}