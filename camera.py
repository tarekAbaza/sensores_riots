from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause

left_button = Button(23)
right_button = Button(24)
camera = PiCamera()

def capture():
    datetime = datetime.now().isoformat()
    camera.capture('/home/pi/%s.jpg' % datetime)

left_button.when_pressed = camera.start_preview
left_button.when_released = camera.stop_preview
right_button.when_pressed = capture
camera.start_preview
capture
pause()