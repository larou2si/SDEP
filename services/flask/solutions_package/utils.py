import json, os
import requests

# to automate our pipeline, we will capture our host IP where the application API is running
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

# define the base_url of our api endpoints
host = "http://"+s.getsockname()[0]+":5000"

def get_user_status(user_id: int, date: str):
    """ 
    request the ENDPOINT to get user status in a specific date
    :param user_id: id of user who made a transaction to by a product
    :param date: date in a string withformat '%Y-%m-%dT%H:%M:%S'
    :return: JSON HTTP Response after requesting the API
    """
    try:
        endpoint1 = host+"/user_status/"+str(user_id)
        params = {'date': date}
        response1 = requests.get(endpoint1, params=params)
        return response1
    except:
        # an error encounter while requesting this API
        raise Exception('USER_STATUS Api unreachable!')

def find_city(ip: str):
    """ 
    request the ENDPOINT to get city name from an IP adress
    :param ip: ip address
    :return: JSON HTTP Response after requesting the API"""
    try:
        endpoint2 = host+"/ip_city/"+ip
        response2 = requests.get(endpoint2)
        return response2
    except:
        # an error encounter while requesting this API
        raise Exception('CITY Api unreachable!')

def read_transactions(path:str):
    """ 
    :param path: file path where we hold a list of transactions.
    :return: json array of transactions """
    try:
        if not os.path.isfile(path):
            raise Exception("Transaction file is not found!")
        f = open(path, 'r')
        file = f.read()
        # the file is not a valid json file! we should clean it up
        file = "["+ file.replace('\n',',').strip(',') +"]"
        f.close()
        return json.loads(file)
    except:
        raise Exception('Unable reading the file as a json format!')
