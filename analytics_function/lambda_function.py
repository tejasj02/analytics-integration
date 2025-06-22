import json
import logging
import boto3
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

cloudwatch = boto3.client("cloudwatch")

def lambda_handler(event, context):
    # Example input: { "latency": 123, "success": true }
    latency = event.get("latency", 0)
    success = 1 if event.get("success", True) else 0

    # Log raw input
    logger.info(f"Received event: {json.dumps(event)}")

    # Emit custom CloudWatch metrics
    cloudwatch.put_metric_data(
        Namespace="AIAnalytics",
        MetricData=[
            {
                "MetricName": "Latency",
                "Value": latency,
                "Unit": "Milliseconds"
            },
            {
                "MetricName": "Success",
                "Value": success,
                "Unit": "Count"
            }
        ]
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Metrics logged."})
    }
