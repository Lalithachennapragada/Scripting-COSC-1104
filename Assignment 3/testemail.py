import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP Configuration
SMTP_SERVER = 'smtp.gmail.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common for Gmail and similar providers
EMAIL_FROM = 'lalithalabcat@gmail.com'  # Sender email
EMAIL_PASSWORD = 'tjwy auzw lgxk cbfx'  # Sender email password
EMAIL_TO = 'lalitha.chennapragada88@gmail.com'  # Recipient email

# Email Content
subject = "SMTP Test Email"
body = "This is a test email sent from a Python script to verify SMTP settings."

try:
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Upgrade to secure connection
    server.login(EMAIL_FROM, EMAIL_PASSWORD)
    server.send_message(msg)
    server.quit()

    print("Email sent successfully!")

except Exception as e:
    print(f"Failed to send email. Error: {e}")