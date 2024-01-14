from httpcore import Response
import requests
import json
from dotenv import load_dotenv
import os
import logging 
import time
import boto3

from flash.commons.utils import TEST_MD_CONTENT, _write_flash, load_text
import boto3

LAMBDA_FUNCTION_ARN="arn:aws:lambda:us-west-2:799492718470:function:flash"
LAMBDA_ENDPOINT="https://imf2z1468l.execute-api.us-west-2.amazonaws.com/default/flash"
AWS_REGION = "us-west-2"

load_dotenv()

class LambdaAgent:

    def __init__(self, technology: str, testing = False) -> None:

        if technology.strip() == "":
            raise RuntimeError("Technology is empty. Did you pass in the correct technology?")
            
        self.technology: str = technology.strip()
        self.testing = testing
        self.learning_material: str = ""
        self.initalize_aws()
        

    def get_learning_material(self) -> str:

        if self.testing:
            logging.debug("Since testing is set to true, returning test page.")
            return TEST_MD_CONTENT

        payload = json.dumps({
            "technology": self.technology
        })

        headers = {
            'x-api-key': os.environ['AWS_LAMBDA_API_KEY'],
            'Content-Type': 'application/json'
        }


        logging.info("Starting request to AWS Lambda")
        start_time = time.time()

        response = self.lambda_client.invoke(FunctionName=LAMBDA_FUNCTION_ARN, Payload=json.dumps(payload))

        # response = requests.request("POST", LAMBDA_ENDPOINT, headers=headers, data=payload)
        logging.debug(f"Response recieved from lambda: {response}")
        logging.info(f"Finished request to AWS Lambda, took {(time.time() - start_time):.2f} seconds")
    
        response_payload = json.loads(response["Payload"].read())
        logging.debug(f"Response payload back from Lambda looks like: {response_payload}")

        response_body = json.loads(response_payload['body'])
        logging.debug(f"Parsed response body looks like: {response_body}")

        self.learning_material = response_body["learning_material"]
        self.to_md(filename=f"{self.technology.replace(' ', '_').lower()}_test.md")

        return self.learning_material
    
    def to_md(self, content: str = "", filename: str = "test_content.md") -> None:
        """
        Writes a string to a local markdown file to folder <project_root>/flash/text_examples/

        Default behaviour writes the current `self.learning_material` to `text_examples/content.md`.
        """
        if content == "":
            content = self.learning_material

        _write_flash(content, f"text-examples/experiments/{filename}")

    def initalize_aws(self) -> None:
        self.session = boto3.Session(profile_name="flash")
        self.lambda_client = self.session.client("lambda", region_name=AWS_REGION)
         