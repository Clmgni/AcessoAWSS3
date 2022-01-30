
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Iniciando aplicação...')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import boto3
from botocore.exceptions import ClientError
import logging

def upload_object(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False

    return True


def create_bucket(bucket_name):
    try:
        s3_client.create_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False

    return True

s3_client = boto3.client(
    's3',
    aws_access_key_id='AKIAQRJVRKK5A5D3XBZH',
    aws_secret_access_key='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'
)

#create_bucket('cjmm-primeirobucket4')

#upload_object('teste.txt', 'cjmm-primeirobucket4')

response = s3_client.list_buckets()

print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

# Resultado:
# Existing buckets:
#   cjmm-primeirobucket
