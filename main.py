import functions_framework
import os
import json
from google.cloud import storage
storage_client = storage.Client()



@functions_framework.http
def list_danmens(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    bucket_name = 'dokis'
    prefix = 'docs/' + request.args.get('doki')
    blobs = storage_client.list_blobs(bucket_name, prefix=prefix)
    
    # PNGファイルの公開URLを取得
    public_urls = []
    for blob in blobs:
        if blob.name.lower().endswith('.svg'):
            public_url = f"https://storage.googleapis.com/{bucket_name}/{blob.name}"
            public_urls.append(public_url)

    # return public_urls

    data = {
        "urls": public_urls
    }

    json_data = json.dumps(data)

    response = json_data
    # response.headers.add('Access-Control-Allow-Origin', '*')  # すべてのオリジンからのアクセスを許可する場合

    return response

