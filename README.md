# ros-notebook

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/MPO-Web-Consulting/ros-notebook/HEAD)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Open in Visual Studio Code](https://img.shields.io/badge/vscode-dev-blue)](https://open.vscode.dev/MPO-Web-Consulting/ros-notebook)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/mpo-web-consulting/ros-notebook/datascience-humble.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/f5e4c6bc6a9d0d407b4b/maintainability)](https://codeclimate.com/github/MPO-Web-Consulting/ros-notebook/maintainability)

ros-notebook is a community maintained [Jupyter Docker Stack](https://jupyter-docker-stacks.readthedocs.io/en/latest/contributing/stacks.html) image that adds [ROS](https://www.ros.org/) to the common notebook containers such as the `datascience-notebook`.

## Tags

### Short Tags

![Latest](https://img.shields.io/badge/Latest-datascience--humble-teal.svg)
![Noetic](https://img.shields.io/badge/Noetic-datascience--noetic-teal.svg)
![Foxy](https://img.shields.io/badge/Foxy-datascience--foxy-teal.svg)
![Humble](https://img.shields.io/badge/Humble-datascience--humble-teal.svg)
![Rolling](https://img.shields.io/badge/Rolling-datascience--rolling-teal.svg)

Short tags are all based on the `datascience-notebook` where `<ros-version>` is the ROS version. For example, `noetic` is a ROS Noetic image based on the `datascience-notebook`.

### All Tags

| ROS | Jupyter |
| --- | ------- |
[![ros](https://img.shields.io/badge/ROS-Noetic-white.svg)](http://wiki.ros.org/noetic) | ![minimal-notebook](https://img.shields.io/badge/Jupyter-Minimal-orange.svg)
[![ros](https://img.shields.io/badge/ROS-Foxy-white.svg)](http://wiki.ros.org/foxy) | ![scipy-notebook](https://img.shields.io/badge/Jupyter-Scipy-orange.svg)
[![ros](https://img.shields.io/badge/ROS-Humble-white.svg)](http://wiki.ros.org/humble) | ![datascience-notebook](https://img.shields.io/badge/Jupyter-Data--Science-orange.svg)
[![ros](https://img.shields.io/badge/ROS-Rolling-white.svg)](http://wiki.ros.org/rolling) | ![tensorflow-notebook](https://img.shields.io/badge/Jupyter-Tensorflow-orange.svg)

All other tags are formed as follows:

`<notebook-type>-<ros-version>`

where `<ros-version>` is the ROS version and `<notebook-type>` is the type of notebook. For example, `minimal-noetic` is a ROS Noetic image based on the `minimal-notebook`.

## Usage

An example `Dockerfile` for a custom notebook image:

```dockerfile
FROM ghcr.io/mpo-web-consulting/ros-notebook:minimal-noetic

# add your customizations here
USER root

RUN mamba install -y tensorflow && \
    mamba clean -y -f && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# switch back to jovyan to avoid accidental container runs as root
USER ${NB_UID}
```

## Development

### install dependencies

```bash
# create a virtual environment
python3 -m venv venv

# activate the virtual environment
source venv/bin/activate

# install the dependencies
pip install -r requirements-dev.txt
```

### Generate Images and Actions

The images and actions are generated from templates using [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/). The templates are located in the `templates` directory. The images are defined in `images.yaml`.

Use the following commands to generate the images and github actions files:

```bash
# generate Dockerfiles for all images
python3 scripts/generate_images.py templates/Dockerfile.j2 images images.yaml

# generate actions for all images
python3 scripts/generate_workflows.py templates/action.yml.j2 images .github/workflows
```
