# Working laibraries 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials
sender = "your_email_address"
receiver_email = "reciver_email_address"
password = "Your_Password"

# Create the email
message = MIMEMultipart() # to get multiple parts like text, HTML and any file 
# Another variables to take data  
message["From"] = sender
message["To"] = receiver_email
message["Subject"] = "Project:- Automated Email from Python"
body = "Hello!\nI am Vishwas Verma. Sorry to desturb you. This is an automated email sent using Python. " \
"My Greetings for you !"
# attache the data in the text file 
message.attach(MIMEText(body, "plain"))

# Send the email
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()   # ugrades connection to secure 
    server.login(sender, password) #login to email id 
    server.sendmail(sender, receiver_email, message.as_string())  #send email as a string 
    print("Email send sucsessfully !")
    server.quit() #quite the server 
except Exception as e:
    print(f"Error:- {e}")
