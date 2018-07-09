"""
Google Cloud Storage Client

This snippet depends on credentials being properly configured using gcloud SDK.
"""
import sys

from google.cloud import storage
from google.cloud.exceptions import NotFound

client = storage.Client()
bucket_name = 'my-bucket-name'
try:
    bucket = client.get_bucket(bucket_name)
except NotFound:
    print("{} does not exist".format(bucket_name))
    sys.exit(1)

# The encryption key should be passed as bytes
# Using a leading forward-slash in the blob path is not necessary
encryption_key = 'c7f32af42e45e85b9848a6a14dd2a8f6'
blob = storage.Blob('path/to/secret', bucket, encryption_key=encryption_key.encode())

# Upload encrypted string to Google Cloud Storage
blob.upload_from_string('my-passphrase')

# There are multiple options for downloading this content

# 1. Download the content as bytes
s = blob.download_as_string()

# 2. Download the content to a writeable file
with open('./secret', 'wb') as fh:
    blob.download_to_file(fh)

# 3. Download the content to a filename
blob.download_to_filename('./secret')
