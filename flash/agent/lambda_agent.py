import requests
import json
from dotenv import load_dotenv
import os

LAMBDA_ENDPOINT="https://imf2z1468l.execute-api.us-west-2.amazonaws.com/default/flash"

load_dotenv()

class LambdaAgent:

    def __init__(self, technology) -> None:
        self.technology = technology

    def get_learning_material(self) -> str:

        payload = {}
        headers = {
            'x-api-key': os.environ['AWS_LAMBDA_API_KEY'],
            'Content-Type': 'application/json'
        }

        response = requests.request("GET", LAMBDA_ENDPOINT, headers=headers, data=payload)

        return response.text