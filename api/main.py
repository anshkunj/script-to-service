from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="Script → Service",
    description="Turn boring scripts into live automation services",
    version="1.0.0",
)

# Register routes
app.include_router(router)


@app.get("/health", tags=["health"])
def health_check():
    return {
        "status": "ok",
        "service": "script-to-service"
    }
