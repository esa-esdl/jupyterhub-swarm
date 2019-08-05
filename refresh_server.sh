#!/bin/bash

# refresh server It will:
#  - removes all running user containers
#  - removes jupyterhub from stack
#  - removes and rebuilds docker image
#  - deploys new image


docker service rm $(docker service ls | grep "jupyter-" | awk '{print $1}')

docker stack rm jupyterhub

# docker needs a moment to release the image we want to delete
sleep 15

docker rmi jupyterhub && docker build -f Dockerfile.jupyterhub -t jupyterhub .

docker stack deploy --compose-file docker-compose.yml jupyterhub

