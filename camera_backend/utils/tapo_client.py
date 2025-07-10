from pytapo import Tapo
from fastapi.concurrency import run_in_threadpool
from models.camera_status import CameraStatus
import logging

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Optionally: configure a default handler if not already configured
if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def _get_device_info(camera: CameraStatus):
    logger.debug(f"Connecting to Tapo camera at {camera.ip}")

    tapo = Tapo(camera.ip, camera.username, camera.password)
    return tapo.getBasicInfo()

def _move_camera(camera: CameraStatus, direction: str):
    logger.debug(f"Connecting to Tapo camera at {camera.ip}")

    tapo = Tapo(camera.ip, camera.username, camera.password)
    if direction == "left":
        return tapo.moveMotor(-10, 0)
    elif direction == "right":
        return tapo.moveMotor(10, 0)
    elif direction == "up":
        return tapo.moveMotor(0, 10)
    elif direction == "down":
        return tapo.moveMotor(0, -10)
    
    logger.warning(f"Invalid move command: {direction}")
    return {"status": "invalid command"}

def _scan_camera(camera: CameraStatus, direction: str):
    logger.debug(f"Connecting to Tapo camera at {camera.ip}")

    tapo = Tapo(camera.ip, camera.username, camera.password)
    if direction == "anticlockwise":
        return tapo.moveMotorCounterClockWise()
    elif direction == "clockwise":
        return tapo.moveMotorClockWise()
    elif direction == "vertical":
        return tapo.moveMotorVertical()
    elif direction == "horizontal":
        return tapo.moveMotorHorizontal()
    
    logger.warning(f"Invalid scan command: {direction}")
    return {"status": "invalid command"}


async def get_camera_status(camera: CameraStatus):
    info = await run_in_threadpool(_get_device_info, camera)
    basic_info = info.get("device_info", {}).get("basic_info", {})
    camera.firmware = basic_info.get("sw_version")
    return camera

async def move_camera(camera: CameraStatus, direction: str):
    return await run_in_threadpool(_move_camera, camera, direction)

async def scan_camera(camera: CameraStatus, direction: str):
    return await run_in_threadpool(_scan_camera, camera, direction)

def get_rtsp_url(camera: CameraStatus) -> str:
    return camera.rtsp_url
