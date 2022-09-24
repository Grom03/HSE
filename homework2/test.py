import unittest
import json
from main_api import app


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_405(self):
        response = self.app.post('/hello')
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.get_data(as_text=True), '')
        response = self.app.get('/set')
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.get_data(as_text=True), '')
        response = self.app.post('/get/1')
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.get_data(as_text=True), '')
        response = self.app.get('/devide')
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.get_data(as_text=True), '')

    def test_hello_good(self):
        response = self.app.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "text/plain")
        self.assertEqual(response.get_data(as_text=True), "HSE One Love!")

    def test_set_415(self):
        response = self.app.post('/set',
                                 headers={})
        self.assertEqual(response.status_code, 415)
        self.assertEqual(response.get_data(as_text=True), '')
        response = self.app.post('/set',
                                 headers={"Content-Type": "text/plain"})
        self.assertEqual(response.status_code, 415)
        self.assertEqual(response.get_data(as_text=True), '')

    def test_set_400(self):
        response = self.app.post('/set',
                                 headers={"Content-Type": "application/json"},
                                 json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_data(as_text=True), '')
        response = self.app.post('/set',
                                 headers={"Content-Type": "application/json"},
                                 json={"key": "1"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_data(as_text=True), '')
        response = self.app.post('/set',
                                 headers={"Content-Type": "application/json"},
                                 json={"value": "1"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_data(as_text=True), '')

    def test_set_good(self):
        response = self.app.post('/set',
                                 headers={"Content-Type": "application/json"},
                                 json={"key": "1", "value": "100"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), '')
        response = self.app.post('/set',
                                 headers={"Content-Type": "application/json"},
                                 json={"key": "1", "value": "101"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), '')

    def test_get_404(self):
        response = self.app.get('/get/2')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_data(as_text=True), '')

    def test_get_good(self):
        response = self.app.post('/set',
                                 headers={"Content-Type": "application/json"},
                                 json={"key": "1", "value": "100"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), '')
        response = self.app.get('/get/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json, {"key": "1", "value": "100"})
        response = self.app.post('/set',
                                 headers={"Content-Type": "application/json"},
                                 json={"key": "1", "value": "101"})
        response = self.app.get('/get/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json, {"key": "1", "value": "101"})

    def test_devide_415(self):
        response = self.app.post('/devide',
                                 headers={})
        self.assertEqual(response.status_code, 415)
        self.assertEqual(response.get_data(as_text=True), '')
        response = self.app.post('/devide',
                                 headers={"Content-Type": "text/plain"})
        self.assertEqual(response.status_code, 415)
        self.assertEqual(response.get_data(as_text=True), '')

    def test_devide_400(self):
        response = self.app.post('/devide',
                                 headers={"Content-Type": "application/json"},
                                 json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_data(as_text=True), '')
        response = self.app.post('/devide',
                                 headers={"Content-Type": "application/json"},
                                 json={"dividend": 1})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_data(as_text=True), '')
        response = self.app.post('/devide',
                                 headers={"Content-Type": "application/json"},
                                 json={"divider": 2})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_data(as_text=True), '')
        response = self.app.post('/devide',
                                 headers={"Content-Type": "application/json"},
                                 json={"dividend": 1, "divider": 0})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_data(as_text=True), '')

    def test_devide_good(self):
        response = self.app.post('/devide',
                                 headers={"Content-Type": "application/json"},
                                 json={"dividend": 1, "divider": 10})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'text/plain')
        self.assertEqual(response.get_data(as_text=True), '0.1')


if __name__ == '__main__':
    unittest.main()
