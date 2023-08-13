import pytest
import requests
from generate_user_list import DataObject
import unittest
import json
from jsonschema import validate

user_schema = {
    "type" : "object",
    "properties" : {
        "code" : {"type" : "number"},
        "type" : {"type" : "string"},
        "message" : {"type" : "string"},
    },
}

def post_request():
        body = DataObject.generate_user_data()
        post_response = requests.post('https://petstore.swagger.io/v2/user/createWithList', json = body) 
        return post_response

def get_request():
    get_response = requests.get('https://petstore.swagger.io/v2/user/' + "ghbsdf@S" ) 
    return get_response

class Test_user_endpoints(unittest.TestCase):

    def test_01_successfull_create_user(self):
        response = post_request()
        self.assertEqual(200, response.status_code)

    def test_02_get(self):
          responce = get_request()
          self.assertEqual(200, responce.status_code)
    
    def test_03_post_json_schema(self):
        response = post_request()
        response_data = response.json()
        validate(instance=response_data, schema=user_schema)
    
         

if __name__ == '__main__':
    unittest.main()
