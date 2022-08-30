# source of this documentation: https://www.youtube.com/watch?v=YZRHqRznO-o

# run the containers
```
docker-compose up -d
```
# access to postgresql container and connect to the DB with
```
psql -U <username> -d <dbname> -W
    enter the password
create table student (id integer primary key, name varchar);
create table course (id integer primary key, name varchar);
```
## until debezium work correctly, we should modify the table
```
ALTER TABLE public.student REPLICA IDENTITY FULL;
ALTER TABLE public.course REPLICA IDENTITY FULL;
```
## set up the debezium connector to this table, we need to create a json file which contains the configuration
### in the terminal run this cmd to set the config
```
curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" 127.0.0.1:8083/connectors/ --data "@debezium.json"
```

### set the kafka topic to listen on our debezium connector (run it again, if you encounter this error: 'Broker: Leader not available')
```
docker run --tty \
    --network debezium_cdc_default \
    confluentinc/cp-kafkacat \
    kafkacat -b kafka:9092 -C \
    -s key=s -s value=avro \
    -r http://schema-registry:8081 \
    -t postgres.public.student
# another terminal:

docker run --tty \
    --network debezium_cdc_default \
    confluentinc/cp-kafkacat \
    kafkacat -b kafka:9092 -C \
    -s key=s -s value=avro \
    -r http://schema-registry:8081 \
    -t postgres.public.course
```

### and now insert some rows in  the DB to capture the events :)
```
insert into student (id,name) values (1, 'karim');
insert into course (id,name) values (1, 'Emotional Intelligence');
```