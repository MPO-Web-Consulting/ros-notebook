# this dockerfile is generated from a template
# do not modify it directly, modify the template instead
# template: templates/ros.Dockerfile.j2

# base image
FROM jupyter/tensorflow-notebook:ubuntu-20.04

USER root

# install ros
# setup timezone and get installation deps
RUN apt-get update && \
    apt-get install -q -y --no-install-recommends \
    dirmngr \
    gnupg2  && \
    rm -rf /var/lib/apt/lists/*

# setup keys
RUN set -eux; \
    key='C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654'; \
    export GNUPGHOME="$(mktemp -d)"; \
    gpg --batch --keyserver keyserver.ubuntu.com --recv-keys "$key"; \
    mkdir -p /usr/share/keyrings; \
    gpg --batch --export "$key" > /usr/share/keyrings/ros1-latest-archive-keyring.gpg; \
    gpgconf --kill all; \
    rm -rf "$GNUPGHOME"

# setup sources.list
RUN echo "deb [ signed-by=/usr/share/keyrings/ros1-latest-archive-keyring.gpg ] http://packages.ros.org/ros/ubuntu focal main" > /etc/apt/sources.list.d/ros1-latest.list

# setup environment
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV ROS_DISTRO noetic

# install ros packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-${ROS_DISTRO}-ros-base \
    build-essential \
    python3-rosdep \
    python3-vcstools \
    python3-rosinstall \
    && rm -rf /var/lib/apt/lists/*

# bootstrap rosdep
RUN rosdep init
# update rosdep
USER ${NB_UID}
RUN rosdep update --rosdistro $ROS_DISTRO


# Source the ROS setup file
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc