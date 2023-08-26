import requests
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
    'id': 'graph1',
    'name': 'Writing Graph',
    'unit': 'Words',
    'color': 'ajisai'
}
requests.post(url=graph_endpt, params=graph_params)
