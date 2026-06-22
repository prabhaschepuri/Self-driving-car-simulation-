import socketio
import eventlet
import numpy as np
import cv2 as cv
import base64

from io import BytesIO
from PIL import Image
from flask import Flask
from tensorflow.keras.models import load_model



# Load Trained Model 

model = load_model(
    r"D:\Self Diving car simulation\Dataset\Self_Driving_model_4.keras",
    compile=False
)

print("Model loaded successfully!")


# Preprocessing before feding into the model

def preprocess(img):

    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    img = img[65:140, :, :]
    img = cv.resize(img, (200, 66))
    img = (img.astype(np.float32) / 127.5) - 1.0    

    return img



# SocketIO and Flask

sio = socketio.Server()
app = Flask(__name__)



# Send Controls (From model predicition to simulator)

def send_control(steering, throttle):

    sio.emit(
        "steer",
        data={
            "steering_angle": str(steering),
            "throttle": str(throttle)
        }
    )


# Connect Event(Connecting the simulator with the python program)
# Intialization of steering and throttle to zero for straight movement intially

@sio.on('connect')
def connect(sid, environ):

    print("Simulator connected!")

    send_control(0, 0)


# Telemetry Event(Data Transfering from simulator to the model)

@sio.on('telemetry')
def telemetry(sid, data):

    if data is None:
        print("No telemetry data")
        return

    print("Telemetry received")

    try:

        speed = float(data["speed"])

        image = Image.open(BytesIO(base64.b64decode(data["image"])))

        image = np.asarray(image)

        image = preprocess(image)

        image = np.expand_dims(image, axis=0)

        pred = model.predict(image,verbose=0)

        print("Prediction:", pred)

        steering = float(pred[0][0])
        steering=np.clip(steering,-0.3,0.3)
        print("Raw:", pred[0][0], "Clipped:", steering)

        # Constant throttle for testing
        throttle = 0.15

        print(f"Speed: {speed}")
        print(f"Steering: {steering}")
        print(f"Throttle: {throttle}")

        send_control(
            steering,
            throttle
        )

    except Exception as e:

        print("ERROR:", e)

# Starts the Server
app = socketio.WSGIApp(
    sio,
    app
)

eventlet.wsgi.server(
    eventlet.listen(('', 4567)),
    app
)
