from minio import Minio
from minio.error import S3Error

# TODO add logging

class MinioConnection:

    def __init__(self, url, username, password):
        self.client = Minio(
            url,
            access_key=username,
            secret_key=password,
            secure=False,  # False because we're using HTTP locally
        )

    def validate_bucket(self, bucket_name):
        if not self.client.bucket_exists(bucket_name):
            self.client.make_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' created successfully.")
        else:
            print(f"Bucket '{bucket_name}' already exists.")
            return

    def delete_bucket(self, bucket_name):
        try:
            self.client.remove_bucket(bucket_name)
        except S3Error as err:
            print(f"MinIO error: {err}")