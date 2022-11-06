import json
import urllib.parse
import boto3
import pickle
from io import BytesIO
import numpy as np

s3 = boto3.client('s3')
bucket = 'rappicardtest'
key = 'RC_modelo_prediccion_fraude.pkl'
model = pickle.loads(boto3.resource('s3').Bucket(bucket).Object(key).get()['Body'].read())

def lambda_handler(event, context):
    try:
        features = event['features']
        result = model.predict_proba([features])[0][1]
        return {
            'statusCode': 200,
            'body': {'result':result}
        }
    except:
        return {
            'statusCode': 404
        }


