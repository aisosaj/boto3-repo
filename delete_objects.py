import boto3

s3 = boto3.client('s3')

bucket = 'hol40aja'
key = 'aws.png'

response = s3.delete_object(
    Bucket=bucket,
    Key=key
    )