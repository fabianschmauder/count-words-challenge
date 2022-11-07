import boto3

s3 = boto3.resource('s3')

def load_s3_object_content(bucket_name, object_key):
    obj = s3.Object(bucket_name, object_key)
    return obj.get()['Body'].read().decode('utf-8') 