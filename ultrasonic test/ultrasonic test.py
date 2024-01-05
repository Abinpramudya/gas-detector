from gpiozero import DistanceSensor
import time

# Define GPIO pins for the ultrasonic sensor
TRIG_PIN = 4  # GPIO pin for the trigger
ECHO_PIN = 17  # GPIO pin for the echo

# Create a DistanceSensor object
ultrasonic_sensor = DistanceSensor(echo=ECHO_PIN, trigger=TRIG_PIN)

try:
    while True:
        distance = ultrasonic_sensor.distance * 100  # Convert to centimeters
        print(f"Distance: {distance:.2f} cm")
        time.sleep(1)

except KeyboardInterrupt:
    # Cleanup GPIO on keyboard interrupt
    ultrasonic_sensor.close()
