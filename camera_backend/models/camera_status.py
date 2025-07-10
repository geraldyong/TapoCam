from pydantic import BaseModel

class CameraStatus(BaseModel):
    id: str
    username: str
    password: str
    password_b64: str
    ip: str
    rtsp_url: str
    firmware: str | None = None

class PanTiltCommand(BaseModel):
    direction: str  # left, right, up, down

