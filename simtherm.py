import time
import random
import requests

# Home Assistant API details
home_assistant_ip = "http://192.168.137.187:8123"  # Replace with your Pi 4's IP address
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJkOWU1ZDdmMjM2Nzg0ZDBkODI4YWJiNmU0MTJmMzZiNCIsImlhdCI6MTczMzYzMzMyMiwiZXhwIjoyMDQ4OTkzMzIyfQ.na9NPP637gwcmKCGHJuZy6m2yC_v729xOB5PDFUYQlU"  # Replace with your Home Assistant token

# Home Assistant entity IDs for temperature and humidity sensor
temperature_entity = "sensor.temperature"
humidity_entity = "sensor.humidity"

# Define headers for the API request
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

# Function to generate simulated temperature and humidity
def generate_simulated_data():
    # Simulate temperature between 18°C and 25°C
    temperature = round(random.uniform(18.0, 25.0), 2)
    # Simulate humidity between 40% and 60%
    humidity = round(random.uniform(40.0, 60.0), 2)
    return humidity, temperature

# Function to send data to Home Assistant
def send_to_home_assistant(temperature, humidity):
    # Prepare data to send to Home Assistant
    temperature_data = {
        "state": temperature,
        "attributes": {
            "unit_of_measurement": "°C",
            "friendly_name": "Temperature",
        },
    }
    humidity_data = {
        "state": humidity,
        "attributes": {
            "unit_of_measurement": "%",
            "friendly_name": "Humidity",
        },
    }

    # Send temperature data
    try:
        temp_response = requests.post(
            f"{home_assistant_ip}/api/states/{temperature_entity}",
            headers=headers,
            json=temperature_data,
        )
        temp_response.raise_for_status()
        print(f"Temperature sent: {temperature}°C")
        
        # Send humidity data
        hum_response = requests.post(
            f"{home_assistant_ip}/api/states/{humidity_entity}",
            headers=headers,
            json=humidity_data,
        )
        hum_response.raise_for_status()
        print(f"Humidity sent: {humidity}%")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to Home Assistant: {e}")

# Main loop to generate simulated data and send to Home Assistant
while True:
    humidity, temperature = generate_simulated_data()

    # Send simulated data to Home Assistant
    send_to_home_assistant(temperature, humidity)
    
    # Wait before taking another reading (e.g., 30 seconds)
    time.sleep(30)
