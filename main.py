import smtplib
import random
import datetime as dt
from dotenv import dotenv_values

config = dotenv_values(".env")
email = config["email"]
password = config["password"]
email2 = config["email2"]

# for i in range(0, 10):
now = dt.datetime.now()
print(now.day)
if now.day == 13:
    with open("quotes.txt") as quotes:
        quotes_list = quotes.readlines()
        quote = random.choice(quotes_list)
        with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=email2, msg=f"Subject: Today's Quote\n\n {quote}")
