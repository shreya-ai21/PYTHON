import smtplib
import datetime as dt

global quotes
# simple mail transfer protocol
email = "shreya.shastry@gmail.com"
password = 'hzlrkiqkxmbnxrzr'

now = dt.datetime.now()
date = now.day
month = now.month
year = now.year
day = now.weekday()


bday = dt.datetime(year=2003, month=7, day=15)

with open("E:/Shreya Shastry/UDEMY/PYTHON/DAY 32/quotes.txt") as file:
    global quotes
    quotes = file.readlines()

msg = {
    0: quotes[0],
    1: quotes[1],
    2: quotes[2],
    3: quotes[3],
    4: quotes[4],
    5: quotes[5],
    6: quotes[6]
}

with smtplib.SMTP('smtp.gmail.com') as connection:

    # tls-transport layer security
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email, to_addrs='shsh.spam1507@gmail.com', msg=msg[day])

# Shreya,shreyarangachar@gmail.com,2003,03,05
# Sahana,sahana.ai21@bmsce.ac.in,2003,05,09
# Shivanshi,shivanshi.ai21@bmsce.ac.in,2002,09,11
# Ruchika,ruchika.ai21@bmsce.ac.in,2002,08,20
# Amma,archana.gowrish@gmail.com,1979,02,09
# Anna,gowrish.bhaskar@gmail.com,1975,01,15
# Ninni,shastry.nischal@gmail.com,2012,10,18
