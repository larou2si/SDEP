# source of this documentation: https://www.youtube.com/watch?v=YZRHqRznO-o

# run the containers
```
docker-compose up -d
```
# access to postgresql container and connect to the DB with
```
psql -U <username> -d <dbname> -W
    enter the password
create table student (id integer primary key, name varchear);
```
## until debezium work correctly, we should modify the table
```
ALTER TABLE public.student REPLICA IDENTITY FULL;
```
## set up the debezium connector to this table, we need to create a json file which contains the configuration
### in the terminal run this cmd to set the config
```
curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" 127.0.0.1:8083/connectors/ --data "@debezium.json"
```

### set the kafka topic to listen on our debezium connector (run it again, if you encounter this error: 'Broker: Leader not available')
```
docker-compose run --tty \
    --network debezium_cdc_default \
    confluentinc/cp-kafkacat \
    kafkacat -b kafka:9092 -C \
    -s key=s -s value=avro \
    -r http://schema-registry:8001 \
    -t postgres.public.student
```

### and now insert some rows in  the DB to capture the events :)

# ERROR: Failed to format message in postgres.public.student [0] at offset 0: Avro/Schema-registry message deserialization: REST request failed (code -1): HTTP request failed: Couldn't connect to server : terminating