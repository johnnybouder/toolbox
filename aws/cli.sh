# Initial setup
aws configure
aws configure --profile [SOME_PROFILE_NAME]

# Get resources
aws ec2 describe-instances
aws s3 ls

# Get EC2 intance metadata
curl http://169.254.169.254/latest/meta-data/