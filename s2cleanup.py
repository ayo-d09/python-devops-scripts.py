import boto3
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Identify empty S3 buckets (dry-run only)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only report empty buckets (default)"
    )
    args = parser.parse_args()

    s3 = boto3.client("s3")
    buckets = s3.list_buckets()["Buckets"]

    for bucket in buckets:
        name = bucket["Name"]
        objects = s3.list_objects_v2(Bucket=name)

        if "Contents" not in objects:
            print(f"EMPTY bucket: {name}")

    if args.dry_run:
        print("Dry-run enabled: no buckets were modified.")

if __name__ == "__main__":
    main()

python s3_cleanup.py --dry-run
