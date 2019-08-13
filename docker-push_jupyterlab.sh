#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push quay.io/esdc/esdl_single_user_lab:$TRAVIS_BRANCH