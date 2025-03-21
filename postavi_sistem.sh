#!/bin/bash

#Ustvari docker omrezje
docker network create app-network

#Naredi streznik
docker build -t server ./server
docker run -d --name server --network app-network server

#Naredi odjemalca
docker build -t client ./client
docker run -d --name client --network app-network client

#Pocakaj 5 sekund, da se vse zazene
sleep 5

#Pridobi in izpise IP naslov odjemalca
IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' client)
echo "IP odjemalca: $IP"