import RPi.GPIO as GPIO
from flask import Flask, request, jsonify

# GPIO pin definitions
RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 24

# Setup GPIO mode and pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# Create PWM instances for each color channel
red_pwm = GPIO.PWM(RED_PIN, 100)
green_pwm = GPIO.PWM(GREEN_PIN, 100)
blue_pwm = GPIO.PWM(BLUE_PIN, 100)

# Start PWM with 0% duty cycle (LEDs off)
red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

# Flask app setup
app = Flask(__name__)

# Function to set RGB color
def set_color(red, green, blue):
    red_pwm.ChangeDutyCycle(red)
    green_pwm.ChangeDutyCycle(green)
    blue_pwm.ChangeDutyCycle(blue)

# Endpoint to control the RGB LED
@app.route('/set_color', methods=['POST'])
def handle_set_color():
    data = request.get_json()
    red = data.get('red', 0)
    green = data.get('green', 0)
    blue = data.get('blue', 0)

    # Clamp values between 0 and 100
    red = max(0, min(100, red))
    green = max(0, min(100, green))
    blue = max(0, min(100, blue))

    set_color(red, green, blue)
    return jsonify({"status": "success", "message": f"Color set to R:{red} G:{green} B:{blue}"}), 200

# Clean up GPIO on shutdown
@app.route('/shutdown', methods=['POST'])
def shutdown():
    set_color(0, 0, 0)
    GPIO.cleanup()
    return jsonify({"status": "success", "message": "GPIO cleaned up, server shutting down"}), 200

# Run the Flask server
if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        set_color(0, 0, 0)
        GPIO.cleanup()
