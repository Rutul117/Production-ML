from fastapi import FastAPI

app = FastAPI(title="Production ML API")


@app.get("/")
def root():
    return {"status": "ok", "service": "production-ml-api"}
