import boto3 #Install using ==> pip install boto3
ec2client = boto3.client('ec2', region_name='eu-west-1')
s3client = boto3.client('s3')

s3List = s3client.list_buckets()
ec2List = ec2client.describe_instances()

print("List out all EC2 instances.")
print('\n')
for reservation in ec2List["Reservations"]:
 for instance in reservation["Instances"]:
  #print(instance)
  print('InstanceId: {}'.format(instance["InstanceId"]))
  print('InstanceType: {}'.format(instance["InstanceType"]))
  print('PrivateDnsName: {}'.format(instance["PrivateDnsName"]))
  print('PrivateIpAddress: {}'.format(instance["PrivateIpAddress"]))
  print('\n')
  
print("List out all S3 buckets.")
print('\n')
#print(s3List)
for bucket in s3List["Buckets"]: 
  print(bucket["Name"])