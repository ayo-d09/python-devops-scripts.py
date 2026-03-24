# Python DevOps Scripts

Simple Python CLI tools demonstrating DevOps-style automation using AWS SDK (boto3).

## Tools & Technologies
- Python 3
- AWS SDK for Python (boto3)
- AWS EC2 & S3
- Linux CLI

## Scripts

### ec2_status.py
Lists all EC2 instances in the configured AWS region and prints their current state.

**Example output:**

### s3_cleanup.py
Identifies empty S3 buckets (dry-run only, no deletion).

**Example output:**

## Setup
bash
pip install boto3
aws configure

python ec2_status.py
python s3_cleanup.py
