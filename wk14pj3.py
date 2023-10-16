import boto3 

ec2 = boto3.client('ec2')

response = ec2.stop_instances(
    InstanceIds=[
        "i-0e4e686bd2e561537", "i-03f43a1d012b89304", "i-047499c1748b41189"
    ]
)