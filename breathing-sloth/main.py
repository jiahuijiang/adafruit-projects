import time
from adafruit_crickit import crickit

motor_1 = crickit.dc_motor_1
motor_2 = crickit.dc_motor_2

## release the residue air
crickit.drive_1.fraction = 1
time.sleep(1)

while True:
    motor_1.throttle = 1
    motor_2.throttle = 1
    crickit.drive_1.fraction = 0
    time.sleep(1.7)
    motor_1.throttle = 0
    motor_2.throttle = 0
    crickit.drive_1.fraction = 1
    time.sleep(3)
