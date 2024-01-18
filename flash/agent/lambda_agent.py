import json
# from dotenv import load_dotenv
import os
import logging 
import time
import boto3
from flash.commons.models import Model

from flash.commons.utils import TEST_MD_CONTENT, _write_flash
import boto3


class LambdaAgent:

    def __init__(self, technology: str, model: Model, testing = False) -> None:

        if technology.strip() == "":
            raise RuntimeError("Technology is empty. Did you pass in the correct technology?")
            
        self.technology: str = technology.strip()
        self.model: Model = model
        self.testing = testing
        self.learning_material: str = ""
        self.initalize_aws()
        

    def get_learning_material(self) -> str:

        if self.testing:
            logging.debug("Since testing is set to true, returning test page.")
            return TEST_MD_CONTENT

        payload = json.dumps({
            "technology": self.technology,
            "model" : self.model.value
        })

        logging.info("Starting request to AWS Lambda")
        start_time = time.time()

        response = self.lambda_client.invoke(FunctionName=os.environ["LAMBDA_FUNCTION_ARN"], Payload=json.dumps(payload))

        # response = requests.request("POST", LAMBDA_ENDPOINT, headers=headers, data=payload)
        logging.debug(f"Response recieved from lambda: {response}")
        logging.info(f"Finished request to AWS Lambda, took {(time.time() - start_time):.2f} seconds")
    
        response_payload = json.loads(response["Payload"].read())
        logging.debug(f"Response payload back from Lambda looks like: {response_payload}")

        response_body = json.loads(response_payload['body'])
        logging.debug(f"Parsed response body looks like: {response_body}")

        self.learning_material = response_body["learning_material"]
        # self.to_md(filename=f"{self.technology.replace(' ', '_').lower()}_test.md")

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
        self.lambda_client = boto3.client("lambda", 
                                          region_name=os.environ["AWS_DEFAULT_REGION"],
                                          aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"], 
                                          aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"])
        logging.info("AWS profile successfully initialized.")
         