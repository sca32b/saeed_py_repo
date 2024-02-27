
# create ann empty dictionary
test_dict = {}
print(test_dict)

test_dict = {"name":"Saeed", "age": 51, "height": 62.5, "movies": ['The Holy Grail', 'The Life of Brian', 'The Meaning of Life']}
gco_dict = {"deploy_name":"eks", "deploy_type":"k8s", "deploy_region": "us-west-2", "deploy_vpc": "vpc-12345678", "deploy_subnet": "subnet-12345678", "deploy_sg": "sg-12345678", "deploy_keypair": "mykeypair", "deploy_ami": "ami-12345678", "deploy_instance_type": "t2.micro", "deploy_min_size": 1, "deploy_max_size": 3, "deploy_desired_capacity": 2, "deploy_asg_name": "myasg", "deploy_lc_name": "mylc", "deploy_lc_ami": "ami-12345678", "deploy_lc_instance_type": "t2.micro", "deploy_lc_keypair": "mykeypair", "deploy_lc_sg": "sg-12345678", "deploy_lc_name": "mylc", "deploy_lc_userdata": "userdata", "deploy_lc_iam_role": "myrole", "deploy_lc_iam_instance_profile": "myprofile", "deploy_lc_security_group": "sg-12345678", "deploy_lc_launch_configuration_name": "mylc", "deploy_lc_launch_configuration_ami": "ami-12345678", "deploy_lc_launch_configuration_instance_type": "t2.micro", "deploy_lc_launch_configuration_keypair": "mykeypair", "deploy_lc_launch_configuration_sg": "sg-12345678", "deploy_lc_launch_configuration_userdata": "userdata", "deploy_lc_launch_configuration_iam_role": "myrole", "deploy_lc_launch_configuration_iam_instance_profile": "myprofile", "deploy_lc_launch_configuration_security_group": "sg-12345678", "deploy_asg_name": "myasg", "deploy_asg_lc_name": "mylc", "deploy_asg_lc_ami": "ami-12345678", "deploy_asg_lc_instance_type": "t2.micro", "deploy_asg_lc_keypair": "mykeypair", "deploy_asg_lc_sg": "sg-12345678", "deploy_asg_lc_userdata": "userdata", "deploy_asg_lc_iam_role": "myrole", "deploy_asg_lc_iam_instance_profile": "myprofile", "deploy_asg_lc_security_group": "sg-12345678", "deploy_asg_lc_launch_configuration_name": "mylc"}

# copy a dictionary
gco_dict_aws = gco_dict

# check if the key doesnt exists in the dictionary
if not "region" in gco_dict:
  gco_dict["region"]="us-east-1"

for k,v in gco_dict.items():
    print(f"{k} : {v}")

# print the copied dictionary
print(gco_dict_aws)

# total items in the dictionary
print(len(gco_dict))


print(test_dict["movies"])
test_dict["sport"]=['soccer', 'cricket', 'hockey']
print(test_dict)

#wipe a dictionary
test_dict = {}
print(test_dict)