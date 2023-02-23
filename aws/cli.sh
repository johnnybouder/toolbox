# Initial setup
aws configure
aws configure --profile [SOME_PROFILE_NAME]

# Get resources
aws ec2 describe-instances
aws s3 ls

# Manually trigger an alarm
aws cloudwatch set-alarm-state ...

# Get EC2 intance metadata
curl http://169.254.169.254/latest/meta-data/

# SSH to EC2 Instance
ssh -i [SOME_KEY.pem] ec2-user@SOME_IP