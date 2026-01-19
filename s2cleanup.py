import boto3

def list_empty_buckets():
    s3 = boto3.client("s3")
    buckets = s3.list_buckets()["Buckets"]

    for bucket in buckets:
        name = bucket["Name"]
        objects = s3.list_objects_v2(Bucket=name)

        if "Contents" not in objects:
            print(f"EMPTY bucket found: {name}")

if __name__ == "__main__":
    list_empty_buckets()
