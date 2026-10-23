import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, attachment_file_path):
    # Create the MIMEMultipart message object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the email body to the message
    msg.attach(MIMEText(body, 'plain'))

    # Attach the file
    try:
        # Open the file in binary mode
        with open(attachment_file_path, "rb") as attachment:
            # Create a MIMEBase object for the attachment
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())

        # Encode the attachment in base64
        encoders.encode_base64(part)

        # Add a header to the attachment
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {attachment_file_path.split('/')[-1]}"
        )

        # Attach the file to the message
        msg.attach(part)

    except Exception as e:
        print(f"Failed to attach file: {e}")
        return

    try:
        # Establish a connection with the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            # Secure the SMTP connection
            server.starttls()

            # Login to the sender's email account
            server.login(sender_email, sender_password)

            # Send the email
            server.send_message(msg)

        print("Email sent successfully with attachment!")

    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
sender_email = ""# Add Your Email
sender_password = ""  # Use an App Password for security
recipient_email = "pythonemailsend01@gmail.com"
subject = "Test Email with Attachment"
body = "This is a test email sent from Python with an attachment!"
attachment_file_path = "d:\krishnaa.jpg"  # Change this to the path of your file

send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, attachment_file_path)
