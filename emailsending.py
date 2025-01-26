import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
sender_email = ''
receiver_email = ''
subject = ''
message = ''
def send_email(sender_email, sender_password, receiver_email, subject, message):
# Create a multipart message object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

# Add the message body
    body = MIMEText(message, 'plain')
    msg.attach(body)

try:
# Create a secure SSL/TLS connection with the SMTP server
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()

# Login to your email account
    server.login(sender_email, sender_password)

# Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    print('Email sent successfully!')
except Exception as e:
    print(f'An error occurred while sending the email: {e}')
finally:
# Close the connection to the SMTP server
    server.quit()

# Example usage
if __name__ == '__main__':
    sender_email = 'sanglesonali4955@gmail.com' # Replace with your email address
    sender_password = 'Sonali@123' # Replace with your email account's password
    receiver_email = 'sanglesonali2000@gmail.com'
    subject = 'Hello from Python!'
    message = 'This is a test email sent using Python.'

    send_email(sender_email, sender_password, receiver_email, subject, message)
