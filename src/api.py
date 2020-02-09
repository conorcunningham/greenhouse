import httpx
import json
from typing import Dict
from datetime import datetime


class Greenhouse:

    def __init__(self, host, username, password):
        self.host = host
        self.user = username,
        self.password = password
        self.token = None
        self.refresh = None
        self.token_timestamp = None
        self.headers = None

    def get_token(self) -> Dict:
        """
        Gets a token for the API
        :return: Dict representing the token or an error message
        """
        url = host + 'token'
        post = httpx.post(
            url, json={"username": username, "password": password}
        )

        if post.status_code == 200:
            self.token = json.loads(post.text)["access"]
            self.refresh = json.loads(post.text)["refresh"]
            self.headers = {"Authorization": "Bearer " + self.token}
            self.token_timestamp = datetime.now()
            return json.loads(post.text)
        else:
            return {"error": "error fecthing token"}

    def fetch_data(self, url: str) -> Dict:
        url = host + url
        data = httpx.get(url, headers=self.headers)
        if data.status_code == 200:
            return json.loads(data.text)
        return {"error": "retieve failed", "errorcode": data.status_code}

    def add_sensor_values(self, data: Dict):
        url = host + "sensor-values"
        request = httpx.post(
            url=url,
            headers=self.headers,
            json=data
        )
        if request.status_code == 201:
            print(request.text)
            return {"success": "successfully created values"}
        return {"error": "error posting", "error_code": request.status_code}

    def add_temperature_values(self, data: Dict):
        url = host + "temperatures"
        request = httpx.post(
            url=url,
            headers=self.headers,
            json=data
        )
        if request.status_code == 201:
            print(request.text)
            return {"success": "successfully created values"}
        print(request.content, request.reason_phrase, request.status_code)
        return {"error": "error posting", "error_code": request.status_code}