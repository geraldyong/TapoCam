from fastapi import APIRouter, HTTPException
from models.camera_status import CameraStatus
from utils.tapo_client import get_camera_status, move_camera, scan_camera, get_rtsp_url
import json
import base64
from pathlib import Path

router = APIRouter()

def load_camera_list() -> list[dict]:
    config_path = Path("config/cameras.json")
    if not config_path.exists():
        raise FileNotFoundError("Camera configuration file not found.")
    with open(config_path) as f:
        cameras = json.load(f)

    for cam in cameras:
        cam["password"] = base64.b64decode(cam["password_b64"]).decode("utf-8")
        cam["rtsp_url"] = f"rtsp://{cam['username']}:{cam['password']}@{cam['ip']}:554/stream1"
    return cameras


def get_camera_or_404(camera_id: str) -> CameraStatus:
    camera_dict = next((c for c in load_camera_list() if c["id"] == camera_id), None)
    if not camera_dict:
        raise HTTPException(status_code=404, detail=f"Camera '{camera_id}' not found.")
    return CameraStatus(**camera_dict)


@router.get("/status/{camera_id}", 
            response_model=CameraStatus,
            summary="Obtain status info from the camera.",
            tags=["Camera Status"])
async def camera_status(camera_id: str):
    camera = get_camera_or_404(camera_id)
    return await get_camera_status(camera)


@router.get("/rtsp-url/{camera_id}",
            summary="Obtain the live feed RTSP URL from the camera.",
            tags=["Camera Feed"])
def camera_rtsp_url(camera_id: str):
    camera = get_camera_or_404(camera_id)
    return {"rtsp_url": get_rtsp_url(camera)}


@router.post("/pan-tilt/{camera_id}",
            summary="Control the camera by moving it up/down/left/right.",
            tags=["Camera Control"])
async def camera_pan_tilt(camera_id: str, direction: str):
    camera = get_camera_or_404(camera_id)
    return await move_camera(camera, direction)


@router.post("/scan/{camera_id}",
            summary="Make the camera do a scan by moving it clockwise/anticlockwise/vertical/horizontal.",
            tags=["Camera Control"])
async def camera_scan(camera_id: str, direction: str):
    camera = get_camera_or_404(camera_id)
    return await scan_camera(camera, direction)