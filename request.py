import requests
import json
import unittest


id = '123' 
wrong_id = '12222'
def create_pet(id):
    body = '{"id":' + id + ',"category": {"id": 2, "name": "sdf"},"name": "doggie","photoUrls": ["string"],"tags": [{ "id": 3,  "name": "string"  }],"status": "available"}'
    body_json = json.loads(body)
    r = requests.post('https://petstore.swagger.io/v2/pet', json=body_json)

class Petendpointtest(unittest.TestCase):

    
        
    def test_create_pet(self):
        body = '{"id":' + id + ',"category": {"id": 2, "name": "sdf"},"name": "doggie","photoUrls": ["string"],"tags": [{ "id": 3,  "name": "string"  }],"status": "available"}'
        body_json = json.loads(body)
        r = requests.post('https://petstore.swagger.io/v2/pet', json=body_json)
        self.assertEqual(200, r.status_code)
        response_id = r.json()["id"]
        expected_response = {"id": response_id, "category": {"id": 2, "name": "sdf"}, "name": "doggie", "photoUrls": ["string"], "tags": [{"id": 3, "name": "string"}], "status": "available"}
        self.assertEqual(expected_response, r.json())

    
    def test_get_pet_id(self):
        create_pet('123')
        r1 = requests.get('https://petstore.swagger.io/v2/pet/123')
        self.assertEqual(200, r1.status_code) 
        response_id = r1.json()["id"]
        expected_response = {"id": response_id, "category": {"id": 2, "name": "sdf"}, "name": "doggie", "photoUrls": ["string"], "tags": [{"id": 3, "name": "string"}], "status": "available"}
        self.assertEqual(expected_response, r1.json())
    
    def test_get_incorrect_id(self):
        r2 = requests.get('https://petstore.swagger.io/v2/pet/' + wrong_id)
        assert r2.headers["Content-Type"] == "application/json"
        self.assertEqual({"code": 1,"type": "error","message": "Pet not found"}, r2.json())
        self.assertEqual(404, r2.status_code) 
    
    def test_update_pet(self):
        body_update = '{"id":' + id + ',"category": {"id": 2, "name": "test"},"name": "test","photoUrls": ["string"],"tags": [{ "id": 3,  "name": "string"  }],"status": "available"}'
        body_json_update = json.loads(body_update)
        r3 = requests.put('https://petstore.swagger.io/v2/pet',json = body_json_update)
        self.assertEqual(200,r3.status_code)
        response_id = r3.json()["id"]
        expected_response = {"id": response_id, "category": {"id": 2, "name": "test"},"name": "test","photoUrls": ["string"],"tags": [{ "id": 3,  "name": "string"  }],"status": "available"}
        self.assertEqual(expected_response, r3.json())

    def test_delete_pet(self):
        r4 = requests.delete('https://petstore.swagger.io/v2/pet/'+ id)
        self.assertEqual(200,r4.status_code)
        response_id = r4.json()["message"]
        expected_response = {"code": 200,"type": "unknown","message": response_id}
        self.assertEqual(expected_response, r4.json())
    
    def test_delete_incorrect_id(self):
        r5 = requests.delete('https://petstore.swagger.io/v2/pet/'+ wrong_id)
        self.assertEqual(404,r5.status_code)

    

if __name__ == '__main__':
    unittest.main()





