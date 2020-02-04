import httpx
import json
from typing import Dict

host = "http://localhost:8000/api/"


def fetch_data(url: str) -> Dict:
    url = host + url
    data = httpx.get(url)
    if data.status_code == 200:
        return json.loads(data.text)
    return {"error": "retieve failed", "errorcode": data.status_code}


def add_sensor_values(data: Dict):
    url = host + "sensor-values"
    request = httpx.post(
        url=url,
        json=data
    )
    if request.status_code == 201:
        print(request.text)
        return {"success": "successfully created values"}
    return {"error": "error posting", "error_code": request.status_code}


def add_temperature_values(data: Dict):
    url = host + "temperatures"
    request = httpx.post(
        url=url,
        json=data
    )
    if request.status_code == 201:
        print(request.text)
        return {"success": "successfully created values"}
    print(request.content, request.reason_phrase, request.status_code)
    return {"error": "error posting", "error_code": request.status_code}