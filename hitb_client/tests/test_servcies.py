import unittest
import requests_mock

from .. import client as hitbctf_client

TEST_DATA_SERVICES = {
     "<service1_id>": "<service1_name>", 
     "<service2_id>": "<service2_name>"
}



def mock(f):
    def wrapped_f(*args, **kwargs):
        with requests_mock.mock() as m:
            m.get('https://ctf.hitb.org/services', json=TEST_DATA_SERVICES)
            f(*args, **kwargs)
    return wrapped_f

class ClientTests(unittest.TestCase):
    
    @mock
    def test_get_teams(self):
        self.assertEqual(hitbctf_client.get_services(), 
           {
             "<service1_id>": "<service1_name>", 
             "<service2_id>": "<service2_name>"
            }
        )