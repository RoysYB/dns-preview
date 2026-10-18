
from fastapi import FastAPI

app = FastAPI(
    title="DNS Preview API",
    description="Preview websites before changing DNS records",
    version="0.1.0",
)


@app.get("/")
def health_check():
    return {
        "service": "DNS Preview API",
        "status": "running",
    }
