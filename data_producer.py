import boto3
import json
import requests
import time

lambda_client = boto3.client("lambda", region_name="us-east-2")  # adjust region if needed

function_name = "AnalyticsFunction"  # use your actual Lambda function name

def generate_payload():
    start = time.time()
    try:
        response = requests.get("https://api.github.com")
        success = response.status_code == 200
    except:
        success = False
    end = time.time()
    
    latency_ms = round((end - start) * 1000, 2)

    return {
        "latency": latency_ms,
        "success": success
    }

def call_lambda():
    payload = generate_payload()
    print(f"Sending: {payload}")
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',
        Payload=json.dumps(payload),
    )
    print("Response:", response["StatusCode"])
    result = json.load(response["Payload"])
    print("Returned:", result)

if __name__ == "__main__":
    for _ in range(5):  # send 5 events
        call_lambda()
        time.sleep(2)
