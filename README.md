# ros-notebook

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![ros](https://img.shields.io/badge/ROS-Noetic-blue.svg)](http://wiki.ros.org/noetic)
[![Open in Visual Studio Code](https://img.shields.io/badge/vscode-dev-blue)](https://open.vscode.dev/MPO-Web-Consulting/ros-notebook)

ros-notebook is a community maintained [Jupyter Docker Stack](https://jupyter-docker-stacks.readthedocs.io/en/latest/contributing/stacks.html) image that adds [ROS](https://www.ros.org/) to the `datascience-notebook`.

## Usage

An example `Dockerfile` for a custom notebook image:

```dockerfile
FROM ghcr.io/mpo-web-consulting/ros-notebook:latest

# add your customizations here
USER root

RUN mamba install -y tensorflow && \
    mamba clean -y -f && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# switch back to jovyan to avoid accidental container runs as root
USER ${NB_UID}
```
