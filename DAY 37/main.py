import requests
from datetime import datetime

now = datetime.now()
# month = now.month
# day = now.day
# if now.month < 10:
#     month = f'0{now.month}'
# if now.day < 10:
#     day = f'0{now.day}'
# datelist = [str(now.year), str(month), str(day)]
# date = ''.join(datelist)
# print(date)

TOKEN = "1BM21AI119"
USERNAME = 'shsh'

pixela_endpt = 'https://pixe.la/v1/users'
params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpt, json=params)
# print(response.text)

graph_endpt = f"{pixela_endpt}/{USERNAME}/graphs"
graph_params = {
    'id': 'graph2',
    'name': 'Coding Graph',
    'unit': 'Code',
    'type': 'int',
    'color': 'ajisai'
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpt, json=graph_params, headers=headers)

post_endpt = f'{graph_endpt}/graph2'
post_params = {
    'date': now.strftime('%Y%m%d'),
    'quantity': '9',
}
response = requests.post(url=post_endpt, json=post_params, headers=headers)
print(response.text)
