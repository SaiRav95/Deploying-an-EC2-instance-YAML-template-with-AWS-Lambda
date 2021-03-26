#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import yaml
import boto3

def lambda_handler(event, context):

    region = 'us-west-1'
                            
    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
                                                    
    print('Bucket: ', bucket, 'Key: ', key)
        
    yaml_file = s3.get_object(Bucket = bucket, Key = key)
        
    record_list = yaml_file['Body'].read().decode('utf-8')
        
    data = yaml.safe_load(record_list)
    
    print('data', data)
    
    print('dataa', data['server']['volumes'][0]['device'])
                                                                
    
    
    AMI = 'ami-0a245a00f741d6301'
    INSTANCE_TYPE = data['server']['instance_type']
    KEY_NAME = 'testfefe'
    REGION = 'us-west-1'
    
    #############
    
    ########## Getting values from the yaml file #################
    
    DEVICE1 = data['server']['volumes'][0]['device']
    DEVICE2 = data['server']['volumes'][1]['device']
    
    SIZE_ROOT_VOLUME = int(data['server']['volumes'][0]['size_gb'])
    
    SIZE_DATA_VOLUME = int(data['server']['volumes'][1]['size_gb'])
    
    MIN_INSTANCES = int(data['server']['min_count'])
    
    MAX_INSTANCES = int(data['server']['max_count'])
    
    SSHKEYPAIR_USER1 = data['server']['users'][0]['ssh_key']
    
    SSHKEYPAIR_USER2 = data['server']['users'][1]['ssh_key']
    
    print('SSHKEYPAIR_USER1', SSHKEYPAIR_USER1)
    
    
    ################################################################
    
    ####Adding userdata script ##############################
    
    user_data = f"""#cloud-config
    cloud_final_modules:
    - [users-groups,always]
    users:
    - name: user1
      groups: [ wheel ]
      sudo: [ "ALL=(ALL) NOPASSWD:ALL" ]
      shell: /bin/bash
      ssh-authorized-keys: 
      - {SSHKEYPAIR_USER1}
    
    
    - name: user2
      groups: [ wheel ]
      sudo: [ "ALL=(ALL) NOPASSWD:ALL" ]
      shell: /bin/bash
      ssh-authorized-keys: 
      - {SSHKEYPAIR_USER2}

    
    """
    
    ######################################################
    
    ### Creating a Security Group ###
 
 
    ec2 = boto3.client('ec2', region_name=REGION)
    
    response = ec2.create_security_group(GroupName='securitygroupfromlambda', Description='fetch')
    security_group_id = response['GroupId']
        
    sg = ec2.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {'IpProtocol': 'tcp',
         'FromPort': 22,
         'ToPort': 22,
         'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
    ])
    
    group_name = 'securitygroupfromlambda'
    response = ec2.describe_security_groups(
    Filters=[
         dict(Name='group-name', Values=[group_name])
    ]
    )
    sg_id = response['SecurityGroups'][0]['GroupId']    
    
    print("New Security Group created")
    
    print('sg_id', sg_id)
    
    
    #### Creating an Instance ####
 
    instance = ec2.run_instances(
        BlockDeviceMappings=[
        {
            'DeviceName': DEVICE1,
            'Ebs': {
                'VolumeSize': SIZE_ROOT_VOLUME

            },
            
        },
        {
            'DeviceName': DEVICE2,
            'Ebs': {
                
                'VolumeSize': SIZE_DATA_VOLUME

            },
        },
    ],
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        MaxCount=MIN_INSTANCES,
        MinCount=MAX_INSTANCES,
        UserData = user_data


    )
        

    print ("New instance created:")
    instance_id = instance['Instances'][0]['InstanceId']
    print (instance_id)
    
    ### Changing Security group from the default to the one we created above ###
    
    launched_change = ec2.modify_instance_attribute(InstanceId=instance_id,Groups=[sg_id])
 
    return instance_id

