#!/bin/bash

export LABBASE_CHANGED=$(git diff --exit-code --name-only | grep labbase)

