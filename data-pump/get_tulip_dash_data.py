''' Get Tulip Dash Data

    This module is the fundmental pumping action of the Tulip Dashboard Data Pump.

    The big idea is that there is a json file with endpoints and filenames - pipelines.json
    This module will open and process the pipelines json file
    Then it will process each pipeline in the file
    then store the resulting data from the pipeline run into the filename

    The API that we're pulling the data from and the bucket we're landing the data stay the same

    So a function and module will help us automate that task and stay flexibile to future evolutions
'''

import requests
import json

from google.cloud import storage

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
    print(f'The pipelines object is: {obj}')
    print(f'The result is: {result.json()}')
