import unittest
import requests_mock

from .. import client as hitbctf_client

TEST_DATA_FLAG_ID = {
    "flag_id_description": "Flag id is a user email",
    "flag_ids": {
        "1": { #Team id
           "host": "10.60.1.3",       
           "flag_ids": ["qyui-asdf-iedj@gmail.com", "mjef-vie4-x4hf@ya.com"]
        }        
    }
}




def mock(f):
    def wrapped_f(*args, **kwargs):
        with requests_mock.mock() as m:
            m.get('https://ctf.hitb.org/flag_ids', json=TEST_DATA_FLAG_ID)
            f(*args, **kwargs)
    return wrapped_f

class ClientTests(unittest.TestCase):
    
    @mock
    def test_get_teams(self):
        self.assertEqual(hitbctf_client.get_flag_id("Mail","test"), 
          {
            "flag_id_description": "Flag id is a user email",
            "flag_ids": {
                "1": { #Team id
                   "host": "10.60.1.3",       
                   "flag_ids": ["qyui-asdf-iedj@gmail.com", "mjef-vie4-x4hf@ya.com"]
                    }        
                }
            }
        )