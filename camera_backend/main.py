from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.camera import router as camera_router

app = FastAPI(
    title="Camera Backend API",
    description="API endpoints for camera control for Tapo Camera."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8001"],  # Adjust this if deployed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(camera_router, prefix="/camera")
