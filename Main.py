import network
import espnow
from machine import Pin, PWM, Timer
from time import sleep, time
import email  # Import the email module

# Setup the LED
led = Pin(13, mode=Pin.OUT)

# Initialize WLAN interface for ESP-NOW communication
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()

# ESP-NOW communication setup
e = espnow.ESPNow()
e.active(True)

# External LED and PWM setup
led_ext = Pin(27, mode=Pin.OUT)
duty_cycle = 100
L1 = PWM(led_ext, freq=500, duty=duty_cycle)

# Distance thresholds for LED control
Low = 200
Med = 500
High = 700

# Timer to track the time spent near the sink
start_time = None
threshold_time = 30  # 30 seconds threshold to increment washed counter
exceed_time = 6 * 60  # 6 minutes threshold to send email in seconds
time_spent = 0  # Time spent at the sink
washed_counter = 0  # Washed counter starts at 0
reward_sent = False  # Flag to ensure reward email is sent only once

while True:
    host, msg = e.irecv(1000)  # Wait for message with a timeout of 1000ms
    if msg:  # msg == None if timeout in recv()
        # Convert bytearray to string
        message_str = msg.decode('utf-8')  # Decode bytearray to string
        
        # Check if the message contains distance and extra information
        if "Distance" in message_str and "Extra" in message_str:
            try:
                # Split message into parts by comma
                parts = message_str.split(',')
                
                # Extract distance value
                distance_str = parts[0].split(':')[1].strip().split()[0]  # Extract the distance value
                distance = float(distance_str)  # Convert to float
                
                # Extract extra value
                extra_str = parts[1].split(':')[1].strip()  # Extract the extra value
                extra = float(extra_str)  # Convert to float if necessary (can keep as string if required)
                
                # Output the parsed data
                print(f"Distance: {distance} cm, Extra: {extra}")
                
                # Track time spent at the sink based on distance
                if 2 < distance <= 120:  # Person is in optimal range (near the sink)
                    if start_time is None:  # Start the timer
                        start_time = time()
                    
                    # Calculate the time spent at the sink
                    time_spent = time() - start_time
                    print(f"Time spent at the sink: {time_spent:.2f} seconds")

                    if time_spent >= threshold_time and washed_counter == 0:  # 30 seconds threshold
                        washed_counter = 1  # Set washed counter to 1 if within range for more than 30 seconds
                        print("Washed counter set to 1")

                    # If time exceeds 6 minutes, send an email
                    if time_spent >= exceed_time:  # Time exceeds 6 minutes
                        email.send_email("You're taking too long and wasting water!")
                        print("Email sent: You're taking too long and wasting water.")

                    # Reward notification if user completes task efficiently
                    if threshold_time <= time_spent < exceed_time and not reward_sent:
                        email.send_email("Great Job!", "You make a difference! I believe in you! You make me want to be a better man!")
                        reward_sent = True  # Ensure email is sent only once
                        print("Email sent: Great Job!")

                    # Turn on/off LEDs based on the distance using specific ranges
                    if distance > 120:
                        led.value(1)  # Turn off the LED
                        L1.freq(10)  # Set PWM frequency to High
                        print('Far')
                    if 80 < distance < 120:
                        led.value(1)  # Turn off the LED
                        L1.freq(500)  # Set PWM frequency to High
                        print('Distracted')
                    if 2 < distance <= 70:
                        led.value(0)  # Turn off the LED
                        L1.freq(10)
                        print('Optimal')

                elif distance > 120:
                    # Reset the timer if distance goes beyond 120 cm
                    start_time = None
                    washed_counter = 0  # Reset washed counter when the person is far away
                    reward_sent = False  # Reset reward email flag
                    print("Person is too far, resetting counter.")

            except ValueError:
                print("Error in parsing distance or extra value")
                
        if message_str == 'end':  # End the loop if message is 'end'
            break
    else:
        print("Error in parsing")
