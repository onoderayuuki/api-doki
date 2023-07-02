import functions_framework
import os
import json
from google.cloud import storage
from flask import Flask, Response

storage_client = storage.Client()



@functions_framework.http
def list_tochus(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    
    # 可変パラメーターを取得
    params = []
    for i in range(0,10):
        param = request.args.get(f'param{i}')
        if param is not None:
            params.append(param)
    
    # HTMLファイルの公開URLを取得 
    bucket_name = 'dokis'
    prefix = 'docs/' + request.args.get('doki', default='')
    blobs = storage_client.list_blobs(bucket_name, prefix=prefix)
    
    public_urls = []
    for blob in blobs:
        if blob.name.lower().endswith('.html'):
            public_url = f"https://storage.googleapis.com/{bucket_name}/{blob.name}"
            public_urls.append(public_url)
    # return public_urls

    # パラメーターと一致するものだけ返却
    match_urls = [url for url in public_urls if any(param in url for param in params)]

    # jsonとして返却
    data = {
        "urls": match_urls
    }

    response = Response(json.dumps(data), mimetype='application/json')
    # response.headers['Access-Control-Allow-Origin'] = 'https://onoderayuuki.github.io'
    # response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    
    return response
