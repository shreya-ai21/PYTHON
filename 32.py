import smtplib
import datetime as dt

global quotes
# simple mail transfer protocol
email="shsh.spam1507@gmail.com"
password='xgclvpxwuzwsziez'

now=dt.datetime.now()
date=now.day
month=now.month
year=now.year
day=now.weekday()


bday=dt.datetime(year=2003,month=7,day=15)

with open("C:\\Users\\Admin\\Downloads\\1bm21ai119\\Python-100-days-of-code\\DAY 32\\quotes.txt") as file:
    global quotes
    quotes=file.readlines()

msg={
    0:quotes[0],
    1:quotes[1],
    2:quotes[2],
    3:quotes[3],
    4:quotes[4],
    5:quotes[5],
    6:quotes[6]
}

with smtplib.SMTP('smtp.gmail.com') as connection:

    # tls-transport layer security
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,to_addrs='shreya.ai21@bmsce.ac.in',msg=msg[day])

