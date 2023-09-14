import requests
import datetime

API_ID = 'dba64191'
API_KEY = '2e55e1c19a532e411663046894f170d0'
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpt = "https://api.sheety.co/b67e5976b2dbd59ef96d61219999495f/myWorkouts/workouts"

GENDER = 'Female'
WEIGHT_KG = 68
HEIGHT_CM = 170
AGE = 20

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(
    exercise_endpoint, json=parameters, headers=headers).json()

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

for exercise in response["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpt, json=sheet_inputs)

    print(sheet_response.text)
