#!/bin/bash
echo "${DOCKER_PASSWORD}" | docker login -u "${DOCKER_USERNAME}" --password-stdin quay.io
docker push quay.io/esdc/esdl_single_user_labbase:${TRAVIS_BRANCH}
docker push quay.io/esdc/esdl_single_user_lab:${TRAVIS_BRANCH}