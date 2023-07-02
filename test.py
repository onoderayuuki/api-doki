#!/usr/bin/env python
from google.cloud import storage

class BlobLister:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name

    def list_blobs(self):
        """Lists all the blobs in the bucket."""

        storage_client = storage.Client()

        # Note: Client.list_blobs requires at least package version 1.17.0.
        blobs = storage_client.list_blobs(self.bucket_name)
        bucket = list(storage_client.list_buckets())
        # Note: The call returns a response only when the iterator is consumed.
        # for blob in blobs:
        #     print(blob.name)
        print(bucket)

if __name__ == "__main__":
    bucket_name = "dokis"  # 実際のバケット名に置き換える

    blob_lister = BlobLister(bucket_name)
    blob_lister.list_blobs()