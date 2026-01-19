import boto3

def main():
    ec2 = boto3.client("ec2")
    response = ec2.describe_instances ()
    
    for reservation in response("Reservations"):
        for instance in reservation ("Instances"):
            print(
                instance["InstanceId"],
                instance["State"]["Name"]
                )
if __name__ == "__main__":
    main()
    