# Deploying-an-EC2-instance-YAML-template-with-AWS-Lambda
Deploying an EC2 instance with two volumes and two users with AWS Lambda Python boto3 which takes YAML file as input.

# Steps to do

1) Create a S3 bucket where we will be uploading our YAML file.
2) Create a lambda function with author from scratch and choose the language as Python 3.8
3) Increase the timeout from the default 3 sec to 5 minutes (The code will not take that long to run it just for safety measure).
4) ------ Create an IAM role which provides EC2FullAccess and S3FullAcess
5) Choose the trigger as a S3 PUT with the bucket (from step 1) where we will be uploading our YAML file.
6) Launch the Lambda function.
7) 
