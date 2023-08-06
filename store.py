import random
import requests
import unittest
import json



rand_id = random.randint(0,1000)
id = str(rand_id)
rand_wrong_id = random.randint(1001,10000)
wrong_id = str(rand_wrong_id)

def create_order(id):
    body = '{"id":' + id + ',"petId": 0,"quantity": 0,"shipDate": "2023-08-06T10:44:43.295Z","status": "placed","complete": true }'
    body_json = json.loads(body)
    post_request = requests.post('https://petstore.swagger.io/v2/store/order', json=body_json)

class StoreEndpointTest(unittest.TestCase):

    def test_place_order(self):
        body = '{"id":' + id + ',"petId": 0,"quantity": 0,"shipDate": "2023-08-06T10:44:43.295Z","status": "placed","complete": true }'
        body_json = json.loads(body)
        post_request = requests.post('https://petstore.swagger.io/v2/store/order', json=body_json)
        self.assertEqual(200, post_request.status_code)
        response_id = post_request.json()["id"]
        expected_response = {"id": response_id,"petId": 0,"quantity": 0,"shipDate": "2023-08-06T10:44:43.295+0000","status": "placed","complete":True }
        self.assertEqual(expected_response, post_request.json())

    def test_get_order_id(self):
        create_order(id)
        get_request_id = requests.get('https://petstore.swagger.io/v2/store/order/'+ id )
        self.assertEqual(200, get_request_id.status_code) 
        response_id = get_request_id.json()["id"]
        expected_response = {"id": response_id,"petId": 0,"quantity": 0,"shipDate": "2023-08-06T10:44:43.295+0000","status": "placed","complete":True }
        self.assertEqual(expected_response, get_request_id.json())

    def test_get_order_incorrect_id(self):
        get_request_incorrect_id = requests.get('https://petstore.swagger.io/v2/store/order/'+ wrong_id)
        assert get_request_incorrect_id.headers["Content-Type"] == "application/json"
        self.assertEqual({'code': 1, 'type': 'error', 'message': 'Order not found'}, get_request_incorrect_id.json())
        self.assertEqual(404, get_request_incorrect_id.status_code) 

    def test_delete_order(self):
        create_order(id)
        delete_request = requests.delete('https://petstore.swagger.io/v2/store/order/'+ id)
        self.assertEqual(200,delete_request.status_code)
        response_id = delete_request.json()["message"]
        expected_response = {"code": 200,"type": "unknown","message": response_id}
        self.assertEqual(expected_response, delete_request.json())

    def test_delete_order_incorrect_id(self):
        delete_request_incorrect_id = requests.delete('https://petstore.swagger.io/v2/store/order/'+ wrong_id)
        self.assertEqual(404,delete_request_incorrect_id.status_code)
        expected_response = {"code": 404,"type": "unknown","message": "Order Not Found"}
        self.assertEqual(expected_response, delete_request_incorrect_id.json())

    def test_get_inventory(self):
        get_request_inventory = requests.get('https://petstore.swagger.io/v2/store/inventory' )
        self.assertEqual(200,get_request_inventory.status_code)
        assert get_request_inventory.headers["Content-Type"] == "application/json"

if __name__ == '__main__':
    unittest.main()