from fastapi import FastAPI

app = FastAPI(title="AI & BI Service", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to AI & BI Platform based on FastAPI"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
