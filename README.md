# Deploying-an-EC2-instance-YAML-template-with-AWS-Lambda
Deploying an EC2 instance with two volumes and two users with AWS Lambda Python boto3 which takes the YAML file as input.


# Description of the code 

The code will create an EC2 instance with two volumes both EBS with different sizes based on the YAML file. It will create a security group with inbound rules in which port 22 listens so you can SSH into it with the users. The Instance will be created in the default VPC with a randomly assigned availability zone without an elastic IP address. The users are created by the userdata which is in the code and the details of the users are given in the YAML file. The public SSH key pairs were provided in the YAML file. The private keys will be provided here in the repository so you can SSH into the instance with the key pair (or you can use your EC2 SSH key pairs). After creating the instance we can connect to the instance using the users via EC2 Instance Connect or SSH Client. We can see that the users can read and write within the instance.

# Things to know 

1) I used the lambda function, bucket, and the deployment of the EC2 instance in **us-west-1** region.
2) I did not create a new VPC I used the dafault one.
3) In the below pic is where I got the AMI and I kept that ID in the code (I got it from "Launch Instances" in the EC2 console).

![Github_AMI_Picture](https://user-images.githubusercontent.com/44057058/112569496-a2d16f00-8dba-11eb-88af-8af491af6ed6.png)

4) I used an existing SSH key pair for the creation of the instance. (In the code it is called testfefe).


# Steps to do

1) Create an S3 bucket where we will be uploading our YAML file.
2) Create a lambda function with "Author from scratch" and choose the language as Python 3.8
3) Increase the timeout from the default 3 sec to 5 minutes (This will ensure that the code will not be timed out).
4) Create an IAM role that provides AmazonEC2FullAccess, AmazonS3FullAccess, and **lambdabasicaccess.json** (lambdabasicaccess.json is in the repository).
5) Attach the IAM role to the Lambda function.
6) Choose the trigger as an S3 PUT with the bucket (from step 1) where we will be uploading our YAML file.
7) Launch the Lambda function.
8) On the top right of code click on "Upload from" and click on ".zip file" and upload **my-deployment-package.zip**.
9) After uploading go to lambda_function.py and **delete the code** which is there and **paste the code** in the file **ec2launch_twovolumes_twousers.py**.
10) We are uploading the zip file because we want lambda to handle YAML data.
11) Click on deploy as you have just changed the code.
12) Create two SSH Key pairs and get their public keys and keep them in the YAML file (The private keys for user1 and user2 are **user1keypair.pem and user2keypair.pem** respectively).
13) Now our YAML file is ready and the code is ready.
14) Now upload the YAML file in the bucket which is the trigger for the lambda function we created.
15) After some time we can see that the EC2 instance and the associated security group are created (The security group will have "securitygroupfromlambda" as the security group name and "fetch" as description).
16) We can see the user data in the EC2 instance in the Actions -> Instance settings -> Edit user data and we can see that the two users (in my case user1 and user2) have been created.
17) You can see that you can connect via EC2 connect using user1 or user2. 
18) You can also connect via SSH and provide the private SSH key for the user for authentication.
19) You can read and write now.


