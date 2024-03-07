
import smtplib
from email.message import EmailMessage

# Email details
sender_email = "muha20311.ec@rmkec.ac.in"
receiver_email = "yaashwin200@gmail.com"
password = "Y@shwin@2002"

# Create the email message
msg = EmailMessage()
msg.set_content("yes")
msg["Subject"] = "Subject of the email"
msg["From"] = sender_email
msg["To"] = receiver_email

# Send the email
try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender_email, password)
    server.send_message(msg)
    print("Email sent successfully")
except Exception as e:
    print(f"Failed to send email. Error: {e}")
finally:
    server.quit()
import random

# List of 12 elements
number_list = [1122,1012,2022,2002,2089,3456,4534,6432,7843,8800,9789]
vehicle_number=["kl10ab8673","tn02ch1100"]
# Generate a random number from the list
random_number = random.choice(number_list)

print(random_number)
