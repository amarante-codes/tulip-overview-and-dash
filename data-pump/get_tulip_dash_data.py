''' Get Tulip Dash Data

    This module is the fundmental pumping action of the Tulip Dashboard Data Pump.

    The big idea is that there is a json file with endpoints and filenames - pipelines.json
    This module will open and process the pipelines json file
    Then it will process each pipeline in the file
    then store the resulting data from the pipeline run into the filename

    The API that we're pulling the data from and the bucket we're landing the data stay the same

    So a function and module will help us automate that task and stay flexibile to future evolutions
'''

import logging
import requests
import json

from google.cloud import storage

def upload_blob_from_memory(bucket_name, destination_blob_name, contents):
    """Uploads a file to the bucket."""

    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The contents to upload to the file
    # contents = "these are my contents"

    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(contents)

    logging.INFO(
        f"{destination_blob_name} with contents {contents} uploaded to {bucket_name}."
    )

# open the pipelines file
pipelines = {}
with open('pipelines.json', 'r') as pl_file:
    pipelines = json.load(pl_file)

data_host = pipelines['pipelineHost']
target_bucket = pipelines['targetBucket']

# process the pipelines
for obj in pipelines['pipelines']:
    # pull the data
    result = requests.get(data_host+obj['endpoint'])
    # store the results
    logging.DEBUG(f'The pipelines object is: {obj}')
    logging.DEBUG(f'The result is: {result.json()}')
    upload_blob_from_memory(target_bucket, obj['targetObject'], result.json())
