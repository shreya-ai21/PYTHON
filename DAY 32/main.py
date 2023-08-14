##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import smtplib
import datetime as dt
import random as rd


file1 = open(
    'E:/Shreya Shastry/UDEMY/PYTHON/DAY 32/letter_templates/letter_1.txt', 'r+')
file2 = open(
    'E:/Shreya Shastry/UDEMY/PYTHON/DAY 32/letter_templates/letter_2.txt', 'r+')
file3 = open(
    'E:/Shreya Shastry/UDEMY/PYTHON/DAY 32/letter_templates/letter_3.txt', 'r+')
file = [file1.readlines(), file2.readlines(), file3.readlines()]


def replace_name(name: str):
    data = rd.choice(file)
    final = []
    for line in data:
        if '[NAME]' in line:
            new_line = line.replace("[NAME]", name, -1)
            line = new_line
        final.append(line)
    send_email(final)


def send_email(message):
    str = ''
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email, to_addrs=to_email, msg=f"Subject:HBD MESSAGE TEST\n\n{str.join(message)}")


# simple mail transfer protocol
email = "shreya.shastry@gmail.com"
password = 'hzlrkiqkxmbnxrzr'

bdays = pd.read_csv('E:/Shreya Shastry/UDEMY/PYTHON/DAY 32/birthdays.csv')
bdays_dict = bdays.to_dict()

now = dt.datetime.now()
date = now.day
month = now.month

for bdate, bmonth in zip(bdays_dict["day"], bdays_dict["month"]):
    if bdays_dict["day"][bdate] == date and bdays_dict["month"][bmonth] == month:
        to_email = (bdays_dict["email"][bdate])
        replace_name(bdays_dict["name"][bdate])
    else:
        print('no')
