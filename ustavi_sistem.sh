#!/bin/bash

sudo docker stop server
sudo docker rm server

sudo docker stop client
sudo docker rm client

sudo docker network rm app-network