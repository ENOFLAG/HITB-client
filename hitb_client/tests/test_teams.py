import unittest
import requests_mock

from .. import client as hitbctf_client

TEST_DATA_TEAMS = {
    "1": { 
        "id": 1,
        "name": "Hackerdom",
        "network": "10.60.1.0/24",
        "logo": "https://ctf.hitb.org/logos/hackerdom.png",
        "country": "RU"
    }, 
}


def mock(f):
    def wrapped_f(*args, **kwargs):
        with requests_mock.mock() as m:
            m.get('https://ctf.hitb.org/teams', json=TEST_DATA_TEAMS)
            f(*args, **kwargs)
    return wrapped_f

class ClientTests(unittest.TestCase):
    
    @mock
    def test_get_teams(self):
        self.assertEqual(hitbctf_client.get_teams(), 
            {
               "1":{
                    "id": 1,
                    "name": "Hackerdom",
                    "network": "10.60.1.0/24",
                    "logo": "https://ctf.hitb.org/logos/hackerdom.png",
                    "country": "RU"
                    }
            }
        )


