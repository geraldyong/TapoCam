# Tapo Camera Microservices

Sets up a FastAPI backend microservice to interact with TP-Link Tapo cameras.
Current endpoints include status checking, pan/tilt control, and RTSP URL retrieval.

This program uses pytapo Python library. For more information, please refer to:
https://github.com/JurajNyiri/pytapo/blob/main/README.md

## Features
- Get camera firmware and status
- Move camera up/down/left/right
- Scan camera in preset patterns
- Retrieve RTSP stream URL

## Prerequisites
Require docker or Kubernetes.

## Setup

### Phone App Setup
1. Set up your Tapo camera via your Tapo app.
2. Set up a camera account and password.
3. Determine the IP of your camera from the app.

### Test Camera
1. Update the `conn_tapo.py` file to put in the right username, password and IP address.
2. Test the connectivity:
   `./conn_tapo.py`

### Run Microservice
1. Update the [config/cameras.json] file. For the password, use convert it to base64.
2. Start up the FastAPI service.
   `./rebuild.sh`
