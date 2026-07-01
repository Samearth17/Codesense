# Necessary libraries
import boto3

# Create an S3 bucket
s3 = boto3.resource('s3')
s3.create_bucket(Bucket='example-bucket')

# Create an EC2 instance
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId= 'ami-035be7bafff33b6b6',
    MinCount=1,
    MaxCount=1,
    KeyName='example-key',
    InstanceType='t2.micro')

# Create a security group
security_group = ec2.create_security_group(
    GroupName= 'example-sg',
    Description= 'example security group')

# Add rules to the security group
security_group.authorize_ingress(
    CidrIp='0.0.0.0/0',
    IpProtocol='-1',
    FromPort='-1',
    ToPort='-1')

# Wait for the instance to start up
ec2.Instance(instance[0].id).wait_until_running()

# Install the necessary libraries
ec2.Instance(instance[0].id).run_command(
    'sudo apt-get install -y python')

ec2.Instance(instance[0].id).run_command(
    'sudo apt-get install -y apache2')

# Write the relevant configuration files
ec2.Instance(instance[0].id).run_command(
    'sudo echo "Hello World" > /var/www/html/index.html')

ec2.Instance(instance[0].id).run_command(
    'sudo echo "Listen 80" > /etc/apache2/ports.conf')

# Restart the service
ec2.Instance(instance[0].id).run_command(
    'sudo systemctl restart apache2')