from json.decoder import JSONDecodeError
import os


if bool(os.getenv('HITBCTF_CLIENT_CACHE')):
    import requests_cache
    requests = requests_cache.CachedSession(
        cache_name='hitbctf',
        backend='redis',
        expire_after=int(os.getenv('HITBCTF_CLIENT_CACHE_EXPIRY', 5)),
        include_get_headers=True,
        old_data_on_error=True
    )
else:
    import requests

ENDPOINT_URL = 'https://ctf.hitb.org'
ENDPOINT_FLAGS = "/flags"
ENDPOINT_TEAMS = "/teams"
ENDPOINT_SERVICES = "/services"
ENDPOINT_FLAG_IDS = "/flag_ids"

def send_flags(flags : list, x_team_token : str) -> None:
    headers = {'X-Team-Token' : x_team_token,'Content-Type':'application/json'}
    response = requests.put(ENDPOINT_URL + ENDPOINT_FLAGS,headers=headers,json=flags) #ToDo Test
    try:
        data = response.json()
    except JSONDecodeError:
        print(response)
        data = {}
    return data

def get_teams() -> None:
    response = requests.get(ENDPOINT_URL+ENDPOINT_TEAMS)
    try:
        data = response.json()
    except JSONDecodeError:
        data = {}
    return data

def get_services() -> None:
    response = requests.get(ENDPOINT_URL+ENDPOINT_SERVICES)
    try:
        data = response.json()
    except JSONDecodeError:
        data = {}
    return data

def get_flag_id(service : str, x_team_token) -> None:
    headers = {'X-Team-Token' : x_team_token}
    payload = {'service' : service}             
    response = requests.get(ENDPOINT_URL+ENDPOINT_FLAG_IDS,params=payload,headers=headers)
    try:
        data = response.json()
    except JSONDecodeError:
        data = {}
    return data
