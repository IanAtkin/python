#!/usr/bin/python3

import logging
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
response = s3.list_buckets()

for bucket in response['Buckets']:

# [{'ApplyServerSideEncryptionByDefault': {'SSEAlgorithm': 'AES256'}}]

  try:
    enc = s3.get_bucket_encryption(Bucket = bucket['Name'])
    if enc['ServerSideEncryptionConfiguration']['Rules'][0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm'] == 'AES256':
      print('{}: {}'.format(bucket['Name'], 'AES256'))
  except:
    print('{}: encryption not configured'.format(bucket['Name']))