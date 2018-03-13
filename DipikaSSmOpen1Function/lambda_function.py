import boto3

def lambda_handler(event, context):
     id = 'i-06d766c918d4b4321'
     command = 'iptables -A INPUT -p tcp --dport 80 -j ACCEPT'
     ssm = boto3.client('ssm')
     ssmresponse = ssm.send_command(InstanceIds=[id], DocumentName='AWS-RunShellScript', Parameters= { 'commands': [command] } )