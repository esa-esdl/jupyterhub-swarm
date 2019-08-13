#!/bin/bash

if [[ ${LABBASE_CHANGED} = 'Dockerfile.jupyterlabbase' ]]
then
  BASE_IMAGE_VERSION=$(grep base_image_version Dockerfile.jupyterlabbase | awk -F '=' '{print $2}')
  docker build -t quay.io/esdc/esdl_single_user_labbase:${BASE_IMAGE_VERSION} -f Dockerfile.jupyterlabbase .
fi