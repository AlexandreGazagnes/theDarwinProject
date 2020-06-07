#! /bin/sh

docker container rm -f infra_cont
docker build -t infraimg . 
docker run -tid  --name infra_cont myimg
docker exec -ti infra_cont /bin/bash