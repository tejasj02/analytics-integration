# AI Analytics

Project Overview:
This project implements a lightweight AI analytics system using AWS Lambda and CloudWatch. It handles incoming data, logs metrics, and visualizes them on a live dashboard.

## Components

lambda_function.py

AWS Lambda function
Logs input and emits custom metrics (Latency, Success)

data_producer.py
Python script to invoke the Lambda with data from api requests
Sends latency values and a success flag

CloudWatch Dashboard

Visualizes Lambda activity and custom metrics in real time

## How to Run

Deploy lambda_function.py as a Lambda in AWS

Runtime: Python 3.11

Add cloudwatch:PutMetricData permission

pip install -r requirements.txt

Run data_producer.py locally

AWS credentials must be configured (use aws configure)

Update region and function name if needed

View metrics on CloudWatch Dashboard


## Dashboard: AnalyticsDashboard
![image](https://github.com/user-attachments/assets/e37fb9b4-617d-453d-bf07-dc5f96cca27c)
Metrics: Invocations, Latency, Success

## Example User Response
```
(venv) PS C:\Users\thete\Github\analytics-integration> python data_producer.py
Sending: {'latency': 68.92, 'success': True}
Response: 200
Returned: {'statusCode': 200, 'body': '{"message": "Metrics logged."}'}
Sending: {'latency': 62.58, 'success': True}
Response: 200
Returned: {'statusCode': 200, 'body': '{"message": "Metrics logged."}'}
Sending: {'latency': 59.98, 'success': True}
Response: 200
Returned: {'statusCode': 200, 'body': '{"message": "Metrics logged."}'}
Sending: {'latency': 62.58, 'success': True}
Response: 200
Returned: {'statusCode': 200, 'body': '{"message": "Metrics logged."}'}
Sending: {'latency': 59.98, 'success': True}
Returned: {'statusCode': 200, 'body': '{"message": "Metrics logged."}'}
Sending: {'latency': 62.58, 'success': True}
Response: 200
Returned: {'statusCode': 200, 'body': '{"message": "Metrics logged."}'}
Sending: {'latency': 59.98, 'success': True}
Response: 200
Returned: {'statusCode': 200, 'body': '{"message": "Metrics logged."}'}
Sending: {'latency': 59.98, 'success': True}
Sending: {'latency': 59.98, 'success': True}
Response: 200
Returned: {'statusCode': 200, 'body': '{"message": "Metrics logged."}'}
Sending: {'latency': 56.21, 'success': True}
Response: 200
Returned: {'statusCode': 200, 'body': '{"message": "Metrics logged."}'}
Sending: {'latency': 61.9, 'success': True}
Response: 200
Returned: {'statusCode': 200, 'body': '{"message": "Metrics logged."}'}
```