import re


def is_valid_email(email):
    # Basic email validation using a regular expression
    pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return bool(re.match(pattern, email))


if __name__ == "__main__":
    to_email = input("Enter recipient's email address: ")

    # Validate the email address
    if not is_valid_email(to_email):
        print("Invalid email address. Please enter a valid email.")
    else:
        subject = input("Enter email subject: ")
        body = input("Enter email body: ")

        send_email(to_email, subject, body)
        print("Email sent successfully!")
