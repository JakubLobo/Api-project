import requests
from datetime import datetime

USERNAME = 'jakublobo'
TOKEN = 'dwajio29184ml:S'
GRAPH_ID = 'graph1'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id': "graph1",
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'sora',
}

headers = {
    'X-USER-TOKEN': TOKEN,
}


today = datetime(year=2023, month=6, day=18)

pixel_config = {
    'date': today.strftime("%Y%m%d"),
    'quantity': '10.00',
}

pixel_post_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'


pixel_update_endpoint = f'{pixel_post_endpoint}/{today.strftime("%Y%m%d")}'

pixel_update_config = {
    'quantity': '5.15',
}


pixel_delete_endpoint = pixel_update_endpoint

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)