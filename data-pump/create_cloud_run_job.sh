#!/bin/bash

JOB_NAME="tulip-data-pump"
IMAGE="us-central1-docker.pkg.dev/bamboo-zephyr-349301/tulip-data-pump-test/tulip-data-pump:latest"

gcloud beta run jobs create $JOB_NAME --image $IMAGE 