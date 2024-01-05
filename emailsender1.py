import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_validator import validate_email, EmailNotValidError


def validate_email_address(email):
    try:
        v = validate_email(email)
        return True
    except EmailNotValidError as e:
        print(str(e))
        return False


def send_email(sender_email, subject, body, gmail_user, gmail_password, server_address, port_number):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = sender_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(server_address, port_number) as server:
            server.starttls()
            server.login(gmail_user, gmail_password)

            # Send the email
            server.sendmail(sender_email, gmail_user, msg.as_string())
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Error: {str(e)}")
    except smtplib.SMTPConnectError as e:
        print(f"SMTP Connection Error: {str(e)}")
    except Exception as e:
        print(f"Error sending email: {str(e)}")


def main():
    # Read credentials from JSON file
    with open('credentials.json') as f:
        credentials = json.load(f)

    # Extract values from the credentials dictionary
    server_address = credentials.get('Server Address')
    gmail_user = credentials.get('gmail_user')
    gmail_password = credentials.get('gmail_password')
    port_number = credentials.get('Port Number')

    # Get user input
    sender_email = input("Enter your email address: ")
    subject = input("Enter the email subject: ")
    body = input("Enter the email body: ")

    # Validate email address
    if not validate_email_address(sender_email):
        print("Invalid email address. Exiting.")
        return

    # Display confirmation
    print("\nEmail Details:")
    print(f"From: {gmail_user}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")

    # Confirm before sending
    confirm = input("\nDo you want to send this email? (yes/no): ").lower()
    if confirm == 'yes':
        send_email(sender_email, subject, body, gmail_user,
                   gmail_password, server_address, port_number)
    else:
        print("Email not sent. Exiting.")


if __name__ == "__main__":
    main()


# SMTP (“Simple Mail Transfer Protocol”), default port 25
# POP3 (“Post Office Protocol version 3”) default port 110
# TCP ("Transmission Control Protocol")
# TLC ("Transport Layer Security") -> encrypts the data
# HTTP - default port 80
# HTTPS - default port 443
