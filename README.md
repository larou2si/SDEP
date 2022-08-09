# SDEP
Software Data Engineer Python




sudo docker rm -vf $(sudo docker ps -aq)
sudo docker rmi -f $(sudo docker images -aq)

sudo docker-compose run --rm app sh -c "python manage.py test && flake8"