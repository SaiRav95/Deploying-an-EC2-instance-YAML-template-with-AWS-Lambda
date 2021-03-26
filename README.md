# Deploying-an-EC2-instance-YAML-template-with-AWS-Lambda
Deploying an EC2 instance with two volumes and two users with AWS Lambda Python boto3 which takes YAML file as input.


# Description of the code 

The code when invoked will create an EC2 instance with two volumes both EBS with different sizes based on the YAML file. It will create a security group with inbound rules in which port 22 is listened so you can SSH into it with the users. The Instance will be created in the default VPC with a randomly assigned availability zone without an elastip IP address. The users are created by the userdata which is in the code and the details of the users are given in the YAML file. The public SSH key pairs were provided in the YAML file. The private keys will be provided here so you can SSH into the instance with the key pair (or you can use your EC2 SSH key pair). After creating the instance we can connect to the instance using the users via EC2 Instance Connect or SSH Client. We can see that the users can read and write within the instance.


# Steps to do

1) Create a S3 bucket where we will be uploading our YAML file.
2) Create a lambda function with "Author from scratch" and choose the language as Python 3.8
3) Increase the timeout from the default 3 sec to 5 minutes (The code will take longer than 3 seconds but not longer than 1 - 2 minutes to run).
4) ------ Create an IAM role which provides AmazonEC2FullAccess and AmazonS3FullAccess.
5) Choose the trigger as a S3 PUT with the bucket (from step 1) where we will be uploading our YAML file.
6) Launch the Lambda function.
7) On the top right of code click on "Upload from" and click on .zip file. Upload my-deployment-package.zip.
8) After uploading go to lambda_function.py and delete the code which is there and paste the code in the file (--------------).
9) We are uploading the zip file because we want lambda to handle yaml data.


