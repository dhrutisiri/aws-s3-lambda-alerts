import json
import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):
    # Get bucket and file info
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    size = event['Records'][0]['s3']['object']['size']  # file size in bytes
    
    message = (
        f"🚨 New file uploaded!\n"
        f"Bucket: {bucket}\n"
        f"File: {key}\n"
        f"Size: {size} bytes"
    )
    
    subject = "S3 Upload Alert"

    # Publish to SNS topic
    sns.publish(
        TopicArn="arn:aws:sns:us-east-2:<ACCOUNT_ID>:S3UploadAlerts",
        Message=message,
        Subject=subject
    )
    
    print(message)
    return {
        'statusCode': 200,
        'body': json.dumps('Alert sent successfully!')
    }
