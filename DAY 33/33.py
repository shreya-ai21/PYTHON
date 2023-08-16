import requests
import datetime
import smtplib
import time

email = "shreya.shastry@gmail.com"
password = 'hzlrkiqkxmbnxrzr'
MY_LAT = 12.971599
MY_LNG = 77.594566


def is_overhead():
    response_iss = requests.get(url='http://api.open-notify.org/iss-now.json')

    response_iss.raise_for_status()

    lat = response_iss.json()["iss_position"]['latitude']
    lon = response_iss.json()["iss_position"]['longitude']

    if MY_LAT-5 <= lat <= MY_LAT+5 and MY_LNG-5 <= lon <= MY_LNG+5:
        return True


def is_night():

    parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0
    }

    response_sun = requests.get(
        url='https://api.sunrise-sunset.org/json?', params=parameters)
    response_sun.raise_for_status()
    data = response_sun.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    now = datetime.datetime.now()
    if now >= sunset or now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_overhead() and is_night:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs='shsh.spam1507@gmail.com',
                                msg="Subject:LOOK UP\n\nISS is above you. Look up.")
