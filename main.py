from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Token Engine Alive"}
# ready for deploy
