import boto3

ec2 = boto3.client('ec2')

response = ec2.stop_instances(
    InstanceIds=[
        'i-0966bed8b69ad8c95', 'i-060b4b68b9e82580c', 'i-0e1b299705726ba81'
    ]
)