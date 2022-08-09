# read the book: 'spark the definitive guide' by Matei Zaharia

# ubuntu
sudo apt update && sudo apt -y full-upgrade

# if necessary to reboot
[ -f /var/run/reboot-required ] && sudo reboot -f

# install or make sure Java is well installed:
$ sudo apt install curl mlocate default-jdk -y
$ java -version

# Download Apache Spark:
wget https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz
tar xvf spark-3.2.1-bin-hadoop3.2.tgz
sudo mv spark-3.2.1-bin-hadoop3.2/ /opt/spark
## Set Spark environment:
gedit ~/.bashrc
    export SPARK_HOME=/opt/spark
    export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
source ~/.bashrc

# Start a standalone master server:
$ start-master.sh
$ sudo ss -tunelp | grep 8080
## start worker
start-worker.sh spark://larou2si:7077