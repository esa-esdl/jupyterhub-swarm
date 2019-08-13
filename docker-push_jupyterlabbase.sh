#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin

BASE_IMAGE_VERSION=$(grep base_image_version Dockerfile.jupyterlabbase | awk -F '=' '{print $2}')
docker push quay.io/esdc/esdl_single_user_labbase:${BASE_IMAGE_VERSION}
