from fastapi import FastAPI,Path,UploadFile,File
import shutil
import pandas as pd
import numpy as np
import io
import boto3
s3_client = boto3.client('s3',
    aws_access_key_id = 'AKIA5B256M6M4Z6LAAHE',
    aws_secret_access_key = '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',
    region_name = 'us-east-1',)

session = boto3.Session(aws_access_key_id='AKIA5B256M6M4Z6LAAHE', aws_secret_access_key='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')
s3 = session.resource('s3')
my_bucket = s3.Bucket('datos-trabajados-databrew')
dataframes = []
for my_bucket_object in my_bucket.objects.all():
    key = my_bucket_object.key
    print(key)
    response = s3_client.get_object(Bucket='datos-trabajados-databrew',Key=key)
    data = response['Body'].read()  
    pq_file = io.BytesIO(data)
    df = pd.read_parquet(pq_file)
    dataframes.append(df)

closed_deals = dataframes[0]
customers = dataframes[1]
marketing = dataframes[2]
order_items = dataframes[3]
order_sellers = dataframes[4]
order_delivered = dataframes[5]
payment_sequentel = dataframes[6]
products = dataframes[7]
reviews = dataframes[8]
orders_No_delivered = dataframes[9]
conexiones_X_estado = dataframes[10]
geolocation = dataframes[11]

app = FastAPI(title='xdxd',description='matenme')

@app.get('/xdxd')
async def get_max_duration(anio:int, plataforma:str, minOSeason:str):
    return {'xd' : 'matenme'}