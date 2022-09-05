import unittest
from starlette.testclient import TestClient

from main import app

client = TestClient(app)


class TestPostcodes(unittest.TestCase):
    def test_valid(self):
        postcode = 'NE22 6EX'
        response = client.get(f"/validate/{postcode}")
        assert response.status_code == 200
        assert response.json()['message'] == "Postcode OK"

    def test_valid_lowercase(self):
        postcode = 'ne22 6ex'
        response = client.get(f"/validate/{postcode}")
        assert response.status_code == 200
        assert response.json()['message'] == "Postcode OK"

    def test_invalid_nospacebetween(self):
        postcode = 'ne226ex'
        response = client.get(f"/validate/{postcode}")
        assert response.status_code == 200
        assert response.json()['message'] == "Postcode OK"

    def test_invalid(self):
        postcode = 'hfhehh'
        response = client.get(f"/validate/{postcode}")
        assert response.status_code == 200
        assert response.json()['message'] == "Postcode invalid"
