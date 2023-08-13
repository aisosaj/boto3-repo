import boto3

ec2 = boto3.client('ec2')

response = ec2.stop_instances(
    InstanceIds=[
        'i-06702aa838a669b10','i-0e32733d5d3d222b3'
    ]
)