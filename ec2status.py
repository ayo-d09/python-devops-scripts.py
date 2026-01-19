import boto3
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="List EC2 instances and their states"
    )
    parser.add_argument(
        "--region",
        default="us-east-1",
        help="AWS region (default: us-east-1)"
    )
    args = parser.parse_args()

    ec2 = boto3.client("ec2", region_name=args.region)
    response = ec2.describe_instances()

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print(
                instance["InstanceId"],
                instance["State"]["Name"]
            )

if __name__ == "__main__":
    main()
