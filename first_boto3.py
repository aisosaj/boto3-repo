import boto3

s3 = boto3.client("s3")

response = s3.create_bucket(
    Bucket='aaim-boto3-81123'
)

print(response)