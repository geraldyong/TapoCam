#!/Users/geraldyong/anaconda3/envs/video/bin/python3

from pytapo import Tapo
import json
import sys

# Replace with your camera's IP address, username, and password
host = "192.168.1.69"
user = "GyCam01"
password = "teVny2Zz"

try:
    print(f"Connecting to Tapo camera at {host}…")
    tapo = Tapo(host, user, password)

    # Get basic device info
    basic_info = tapo.getBasicInfo()
    print("\n📷 Basic Info:")
    print(json.dumps(basic_info, indent=2))

    # Get stream URL
    stream_url = tapo.getStreamURL()
    print(f"\n🎥 Stream URL: {stream_url}")

    # Inference: camera is online if we got here
    print("\n✅ Camera is online and responding.")

except Exception as e:
    print(f"\n❌ Error connecting to Tapo camera: {e}")
    sys.exit(1)
