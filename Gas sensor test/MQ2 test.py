from gpiozero import MCP3008
import time

# Define GPIO pin for the analog output of the MQ2 sensor
MQ2_PIN = 4  # You may need to adjust this pin based on your wiring

# Create an MCP3008 object for ADC
adc = MCP3008(channel=MQ2_PIN)

def read_mq2_value():
    # Read analog value from the MQ2 sensor
    sensor_value = adc.value
    return sensor_value

try:
    while True:
        mq2_value = read_mq2_value()
        
        # Map the sensor value to a gas concentration range (adjust based on your sensor's characteristics)
        gas_concentration = (mq2_value - 0.2) / 0.6 * 100.0
        gas_concentration = max(0, min(100, gas_concentration))  # Ensure the value is between 0 and 100
        
        print(f"MQ2 Sensor Value: {mq2_value:.2f}, Gas Concentration: {gas_concentration:.2f}%")
        time.sleep(1)

except KeyboardInterrupt:
    # Cleanup GPIO on keyboard interrupt
    pass
