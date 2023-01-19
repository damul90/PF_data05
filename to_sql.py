import pandas as pd
import requests as req
import pymysql as sql
import numpy as np
from sqlalchemy import create_engine



closed_deals = pd.read_csv('./DataSets_clean/closed_deals.csv')
customers = pd.read_csv('./DataSets_clean/customers.csv')
geolocation = pd.read_csv('./DataSets_clean/geolocation.csv')
marketing_qualified_leads = pd.read_csv('./DataSets_clean/marketing_qualified_leads.csv')
order_items = pd.read_csv('./DataSets_clean/order_items.csv')
order_payments = pd.read_csv('./DataSets_clean/order_payments.csv')
order_reviews = pd.read_csv('./DataSets_clean/order_reviews.csv')
orders_delivered = pd.read_csv('./DataSets_clean/orders_delivered.csv')
orders_No_delivered = pd.read_csv('./DataSets_clean/orders_No_delivered.csv')
products = pd.read_csv('./DataSets_clean/products.csv')
sellers = pd.read_csv('./DataSets_clean/sellers.csv')
conectividad_X_Estado = pd.read_csv('./DataSets_clean/conectividad_X_Estado.csv')

engine = create_engine('mysql+pymysql://root:admin@localhost/olist')

closed_deals.to_sql('closed_deals',con=engine,if_exists='replace')
customers.to_sql('customers',con=engine,if_exists='replace')
geolocation.to_sql('geolocation',con=engine,if_exists='replace')
marketing_qualified_leads.to_sql('marketing_qualified_leads',con=engine,if_exists='replace')
order_items.to_sql('order_items',con=engine,if_exists='replace')
order_payments.to_sql('order_payments',con=engine,if_exists='replace')
order_reviews.to_sql('order_reviews',con=engine,if_exists='replace')
orders_delivered.to_sql('orders_delivered',con=engine,if_exists='replace')
orders_No_delivered.to_sql('orders_No_delivered',con=engine,if_exists='replace')
products.to_sql('products',con=engine,if_exists='replace')
sellers.to_sql('sellers',con=engine,if_exists='replace')
conectividad_X_Estado.to_sql('conectividad_X_Estado',con=engine,if_exists='replace')