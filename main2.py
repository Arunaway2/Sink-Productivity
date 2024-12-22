import network
import espnow
from hcsr04 import HCSR04
from time import sleep

# Initialize WLAN interface for ESP-NOW
sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
sta.active(True)
sta.disconnect()  # For ESP8266

# Initialize the HC-SR04 ultrasonic sensor
sensor = HCSR04(trigger_pin=14, echo_pin=32, echo_timeout_us=10000)
    

# Initialize ESP-NOW
e = espnow.ESPNow()
e.active(True)

# Define the peer's MAC address (replace with actual MAC)
peer = b'\x14\x2b\x2f\xaf\x58\x58'  # MAC address of peer's wifi interface
e.add_peer(peer)  # Must add_peer() before send()



# Send a startup message to the peer
e.send(peer, "Starting...")9

# Main loop to continuously read distance and send data via ESP-NOW
# Main loop to continuously read distance and send data via ESP-NOW
extra_value = 30  # Start with an initial value

while True:
 
    distance = sensor.distance_cm()  # Read the distance in cm from the sensor
    print(distance)
    
    # Oscillate the extra_value between 0 and 1
    extra_value = 31 - extra_value  # Toggle between 0 and 1
    
    message = f'Distance: {distance:.0f} cm, Extra: {extra_value}'  # Send both distance and oscillating value
    
    print(message)  # Print the message locally
    e.send(peer, message)  # Send the message to the peer
    sleep(.01)  # Wait for 1 second before the next reading
    
    
    

