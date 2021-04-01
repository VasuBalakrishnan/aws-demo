import logging
import boto3
from botocore.exceptions import ClientError


def get_account_id():
    return boto3.client('sts').get_caller_identity().get('Account')

def list_buckets():
    s3 = boto3.resource('s3')

    for bucket in s3.buckets.all():
        print(bucket.name)

def bucket_exists(bucket):
    s3 = boto3.resource('s3')
    return s3.Bucket(bucket) in s3.buckets.all()

def create_bucket(bucket_name):
    try:
        if not bucket_exists(bucket_name):
            s3 = boto3.client('s3')
            s3.create_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

if __name__ == "__main__":
    # list_buckets()
    account_id = get_account_id()
    print(account_id)
    create_bucket(f'test-{account_id}')
    list_buckets()