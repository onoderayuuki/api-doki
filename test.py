#!/usr/bin/env python
from google.cloud import storage
import json

class BlobLister:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name

    def list_blobs(self):
        """Lists all the blobs in the bucket."""

        storage_client = storage.Client()

        # Note: Client.list_blobs requires at least package version 1.17.0.
        # bucket = list(storage_client.list_buckets())
        # print(bucket)
        
        blobs = storage_client.list_blobs('dokis')

        # Note: The call returns a response only when the iterator is consumed.
        # for blob in blobs:
        #     print(blob.name)
        
        prefixes = []
        for blob in blobs:
            prefix = blob.name.split('/')[1]  # '/'で分割し、2番目の要素を取得
            prefixes.append(prefix)
        # print(prefixes)
        unique_prefixes = sorted(list(set(prefixes)))
        # print(unique_prefixes)

        data = {
            "names": unique_prefixes
        }

        json_data = json.dumps(data)

        print(json_data)


if __name__ == "__main__":
    bucket_name = "dokis"  # 実際のバケット名に置き換える

    blob_lister = BlobLister(bucket_name)
    blob_lister.list_blobs()
    # get_folder_names()