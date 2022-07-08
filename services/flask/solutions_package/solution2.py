#!/usr/bin/env python3

import pandas as pd
from utils import find_city, get_user_status, read_transactions


path = "../transactions.json"
transactions = read_transactions(path)

# extract features from APIs to add user_status and city of specific trasaction processed
for click in transactions:
    respone_user_status = get_user_status(click['user_id'], click['created_at'])
    if respone_user_status.status_code!=200: 
        # if there is an error, we break this iteration and move to the next click  
        continue
    click['user_status'] = respone_user_status.json()['user_status']
    
    respone_city = find_city(click['ip'])
    if respone_city.status_code!=200: 
        # if there is an error, we break this iteration and move to the next click  
        continue
    click['city'] = respone_city.json()['city']

# transform the transaction in a DataFrame
df = pd.DataFrame(transactions)
# we group out transactions by 'user_status','city' then, we sum the product_price
g = df.groupby(['user_status','city'])['product_price'].sum()


print(g.to_dict())

# demande the type of file where we will save our results
output_filename = 'output/product_price_aggregation2'
x = input("Would you like to save the results? 1:csv / 2:json")
if x=='1':
    g.to_csv(output_filename+'.csv')
elif x=='2':
    g.to_json(output_filename+'.json')
