"""Test create dataset
@Author: NguyenKhacThanh
"""

from voluptuous import Schema, All, Required, Length
from tests.api import APITestCase


class CreateDatasetTestCase(APITestCase):
    def url(self):
        return "/dataset"

    def method(self):
        return "POST"

    def test_success(self):
        payload = {
            "number_of_input": 3
        }
        code, body = self.call_api(content=payload)
        assert 200 == code, body["message"]
        schema = Schema({
            Required("id"): All(str, Length(24)),
            Required("message"): str
        })
        schema(body)

        # remove dataset
        code, body = self.call_api(
            url=f"/dataset/{body['id']}",
            method="DELETE"
        )
        assert code == 200, body["message"]

    def test_none_payload(self):
        payload = {}
        code, body = self.call_api(content=payload)
        assert 400 == code, body["message"]

    def test_no_input_less_than_one(self):
        payload = {
            "number_of_input": 0
        }
        code, body = self.call_api(content=payload)
        assert 400 == code, body["message"]
