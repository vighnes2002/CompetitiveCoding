from azure.storage.blob import BlobClient

blob = BlobClient.from_connection_string(
    conn_str="DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=storageblobtestnewazure;AccountKey=qGMgf8tEcWpYn0tavitMjsH8sBQv5OLy09egB8OvT91zJC7cpYtjWvn2nANFxb2oFBiVOOjjsDPc+AStyXzK8w==;BlobEndpoint=https://storageblobtestnewazure.blob.core.windows.net/;FileEndpoint=https://storageblobtestnewazure.file.core.windows.net/;QueueEndpoint=https://storageblobtestnewazure.queue.core.windows.net/;TableEndpoint=https://storageblobtestnewazure.table.core.windows.net/", container_name="containertest", blob_name="firstBlob")

with open("./sample.txt", "rb") as data:
    blob.upload_blob(data)
