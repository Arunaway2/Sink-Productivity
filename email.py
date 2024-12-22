# Complete project details: https://RandomNerdTutorials.com/micropython-send-emails-esp32-esp826/
# Micropython lib to send emails: https://github.com/shawwwn/uMail
import umail
import network

# Your network credentials
ssid = 'Berkeley-IoT'
password = 'Ti,10a1I'

# Email details
sender_email = 'arunaabhayadavalli@gmail.com'
sender_name = 'ESP32' #sender name
sender_app_password = 'ijxmghtutioojyks'
recipient_email ='arunaway@berkeley.edu'
email_subject ='Someone has forgotten to clean their dishes'

def connect_wifi(ssid, password):
  #Connect to your network
  station = network.WLAN(network.STA_IF)
  station.active(True)
  station.connect(ssid, password)
  while station.isconnected() == False:
    pass
  print('Connection successful')
  print(station.ifconfig())
    
# Connect to your network
connect_wifi(ssid, password)




# Send the email
smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True) # Gmail's SSL port
smtp.login(sender_email, sender_app_password)
smtp.to(recipient_email)
smtp.write("From:" + sender_name + "<"+ sender_email+">\n")
smtp.write("Subject:" + email_subject + "\n")
smtp.write("Hello from ESP32")
smtp.send()
smtp.quit()


