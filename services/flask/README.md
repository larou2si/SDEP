## Description

### API


#### Endpoint user_status
`/user_status/<user_id>?date=2017-10-10T10:00:00`

#### Endpoint city
`/ip_city/10.0.0.0`

On this endpoint please provide an implementation that searches the provided IP ranges and returns the correct city based on the IP.
In case the IP range is not within any of the provided cities, **unknown** should be returned.

### File Processing

Please read the file `transactions.json` and enrich it with the data given by the API.
The output of the script should provide an aggregate containing the sum of `product_price` grouped by `user_status` and `city`.


## To test the application
the Project Folder Tree as follow:
```
Project
├── api.py
├── exceptions.py
├── solutions_package
│   └── output , this folder holds the results of our scripts 
│   └── __init__.py
│   └── utils.py , an essential module where the abstract and reusable functions are implemented 
│   └── solution1.py , a script that handle the sum of product price while iterating the transactions one by one successively
│   └── solution2.py , a perspective of script to aggregate using pandas package
└── README.md
└── requuirements.txt
└── transactions.json
```

To run the API just run the api.py file.
```
pip install -r requirements.txt
python api.py
```

Follow these instructions to run the python scipt in order to display or save Product Price grouped by user status and city:
```
cd solutions_package
python solution1.py
python solution2.py
```

