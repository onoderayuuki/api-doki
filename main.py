import functions_framework

from google.cloud import storage
from flask import Flask, Response

storage_client = storage.Client()

def copy(source_blob,file_name,new_file_name):
    destination_bucket_name = 'doki_pcl'
    destination_bucket = storage_client.bucket(destination_bucket_name)
    destination_blob_name = 'test/'+file_name.replace('.pcl', new_file_name)
    destination_blob = destination_bucket.blob(destination_blob_name)
    
    source_blob.download_to_filename('/tmp/' + file_name)
    destination_blob.upload_from_filename('/tmp/' + file_name)

    return f'File {file_name} copied to {destination_blob_name}.'

@functions_framework.http
def tests(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    
    # バケットとファイル名の設定
    source_bucket_name = 'doki_pcl'
    file_name = 'TEST20230514-J01-01.ply'  # トリガーとなったファイル名を取得

    # 1.ファイル読み込み
    source_bucket = storage_client.bucket(source_bucket_name)
    pcd_file = source_bucket.blob(file_name)


    # 別のバケットにファイルを保存
    response = copy(pcd_file,file_name,'00.pcl')

    # response.headers['Access-Control-Allow-Origin'] = 'https://onoderayuuki.github.io'
    # response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response
