#!/usr/bin/env python3

import json
from utils import find_city, get_user_status, read_transactions


path = "../transactions.json"
transactions = read_transactions(path)


result = {} # while iterating the transaction, we save user_status_city as a unique than we append product_proce to its value


# extract features from APIs to add user_status and city of specific trasaction processed
for click in transactions:
    respone_user_status = get_user_status(click['user_id'], click['created_at'])
    if respone_user_status.status_code!=200: 
        # if there is an error, we break this iteration and move to the next click  
        continue
    user_status = respone_user_status.json()['user_status']
    click['user_status'] = user_status

    respone_city = find_city(click['ip'])
    if respone_city.status_code!=200: 
        # if there is an error, we break this iteration and move to the next click  
        continue
    city = respone_city.json()['city']
    click['city'] = city

    key = user_status+'_'+city
    if not key in result.keys():
        result[key] = click['product_price']
    else:
        result[key] += click['product_price']

print(result)

# save the results in a file
output_filename = 'output/product_price_aggregation1.json'
f=open(output_filename, 'w')
f.write(json.dumps(result))
f.close()