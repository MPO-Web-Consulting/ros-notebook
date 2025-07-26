# a testing Dockerfile to see if the ros package repos are still available
FROM ghcr.io/mpo-web-consulting/ros-notebook:latest

# set root user
USER root

# update base image
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*
