
import ipaddress

from fastapi import FastAPI
from pydantic import BaseModel, field_validator

# 1. Create the application before using @app decorators
app = FastAPI(
    title="DNS Preview API",
    description="Preview websites before changing DNS records",
    version="0.1.0",
)


# 2. Define the expected request data
class PreviewRequest(BaseModel):
    domain: str
    destination_ip: str

    @field_validator("domain")
    @classmethod
    def validate_domain(cls, value: str) -> str:
        value = value.strip().rstrip(".").lower()

        if not value or "." not in value:
            raise ValueError("Enter a valid domain, such as example.com")

        return value

    @field_validator("destination_ip")
    @classmethod
    def validate_destination_ip(cls, value: str) -> str:
        value = value.strip()

        try:
            ipaddress.ip_address(value)
        except ValueError as exc:
            raise ValueError(
                "Enter a valid IPv4 or IPv6 address"
            ) from exc

        return value


# 3. Health-check endpoint
@app.get("/")
def health_check():
    return {
        "service": "DNS Preview API",
        "status": "running",
    }


# 4. Preview input endpoint
@app.post("/api/previews")
def create_preview(request: PreviewRequest):
    return {
        "message": "Input validated successfully",
        "domain": request.domain,
        "destination_ip": request.destination_ip,
        "preview_ready": False,
    }
