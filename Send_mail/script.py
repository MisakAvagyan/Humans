import smtplib
from email.mime.text import MIMEText
from getpass import getpass


def send_mail(text):
    email = input('Enter your email - ')
    recipient_email = input('Enter the recipient_email - ')
    password = getpass("Enter your Gmail password (or application-specific password) - ")

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(email, password)
        txt = MIMEText(text)
        txt['Subject'] = input('YOUR TOPIC - ')
        server.sendmail(email, recipient_email, txt.as_string())
        return 'Successful!'
    except Exception as e:
        return str(e), 'Something went wrong'


def main():
    text = input('Write the message - ')
    print(send_mail(text))


if __name__ == '__main__':
    main()
