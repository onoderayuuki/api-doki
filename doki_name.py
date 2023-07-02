import functions_framework
import os
import json
from google.cloud import storage
storage_client = storage.Client()



@functions_framework.http
def doki_name(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """

    blobs = storage_client.list_blobs('dokis')

    prefixes = []
    for blob in blobs:
        prefix = blob.name.split('/')[1]  # '/'で分割し、2番目の要素を取得
        prefixes.append(prefix)

    unique_prefixes = sorted(list(set(prefixes)))

    data = {
        "names": unique_prefixes
    }

    json_data = json.dumps(data)

    return json_data

