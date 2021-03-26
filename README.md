# Deploying-an-EC2-instance-YAML-template-with-AWS-Lambda
Deploying an EC2 instance with two volumes and two users with AWS Lambda Python boto3 which takes YAML file as input.


# Description of the code 

The code when invoked will create an EC2 instance with two volumes both EBS with different sizes based on the YAML file. It will create a security group with inbound rules in which port 22 is listened so you can SSH into it with the users. The Instance will be created in the default VPC with a randomly assigned availability zone without an elastip IP address. The users are created by the userdata which is in the code and the details of the users are given in the YAML file. The public SSH key pairs were provided in the YAML file. The private keys will be provided here so you can SSH into the instance with the key pair (or you can use your EC2 SSH key pair). After creating the instance we can connect to the instance using the users via EC2 Instance Connect or SSH Client. We can see that the users can read and write within the instance.

# Things to know 

1) I used the lambda function, bucket, and the deployment of the EC2 instances in us-west-1 region.
2) Did not create a new VPC I used the dafault one.
3) I used an existing key pair for the creation of the instance. (In the code it is called testfefe).
4) ![Github_AMI_Picture](https://user-images.githubusercontent.com/44057058/112569496-a2d16f00-8dba-11eb-88af-8af491af6ed6.png)




# Steps to do

1) Create a S3 bucket where we will be uploading our YAML file.
2) Create a lambda function with "Author from scratch" and choose the language as Python 3.8
3) Increase the timeout from the default 3 sec to 5 minutes (The code will take longer than 3 seconds but not longer than 1 - 2 minutes to run).
4) Create an IAM role which provides AmazonEC2FullAccess, AmazonS3FullAccess, and lambdabasicaccess.json.
5) Choose the trigger as a S3 PUT with the bucket (from step 1) where we will be uploading our YAML file.
6) Launch the Lambda function.
7) On the top right of code click on "Upload from" and click on .zip file. Upload my-deployment-package.zip.
8) After uploading go to lambda_function.py and delete the code which is there and paste the code in the file (--------------).
9) We are uploading the zip file because we want lambda to handle yaml data.
10) Click on deploy as you have just changed the code.
11) Create two SSH Key pairs and get their public keys and keep them in the YAML file.
12) Now our YAMl file is ready and the code is ready.
13) Now upload the YAML file in the bucket which is the trigger for the lambda function we created.
14) We can see that EC2 instance and the associated security group are created.
15) We can see the user data in the ec2 instance in the instance settings and we can see that the two users (in my case user1 and user2) have been created.
16) 


