from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "Ali Siddiqui"
message["to"] = "alisiddiqui465@gmail.com"
message["subject"] = "just a test email"
message.attach(MIMEText("This is just a test email sent by using python!!!"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # email and password has been changed before posting on github
    smtp.login("abc@gmail.com", "abcabcThisIsAPassword")
    smtp.send_message(message)
    print("Sent...")
