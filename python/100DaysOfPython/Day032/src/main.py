# Day 32 - 'Happy Birthday Card' email
# Send email via SMTP
import random
import smtplib
import datetime as dt


def exercise1(msg: str) -> None:
    gmail_smtp: str = "smtp.gmail.com"
    gmail_smtp_port: int = 587

    email: str = ""
    password: str = ""

    email_to: str = ""

    #msg: str = "testing"

    connection: smtplib = smtplib.SMTP(gmail_smtp, port=gmail_smtp_port)
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs=[email, email_to], msg=msg)


def exercise2() -> None:
    time_now: dt = dt.datetime.now()
    week_day: dt = time_now.weekday()

    if week_day == time_now.weekday():
        with open("./data/quotes.txt") as file:
            quotes = file.readlines()

        random_num: int = random.randint(0, len(quotes)-1)
        msg: str = quotes[random_num]

        exercise1(msg)


#exercise1(msg)  # Send Email
exercise2() #  from quotes.txt, select one and Send Email
