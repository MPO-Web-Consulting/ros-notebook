# ros-notebook

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/MPO-Web-Consulting/ros-notebook/HEAD)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Open in Visual Studio Code](https://img.shields.io/badge/vscode-dev-blue)](https://open.vscode.dev/MPO-Web-Consulting/ros-notebook)

ros-notebook is a community maintained [Jupyter Docker Stack](https://jupyter-docker-stacks.readthedocs.io/en/latest/contributing/stacks.html) image that adds [ROS](https://www.ros.org/) to the common notebook containers such as the `datascience-notebook`.

## Tags

| ROS | Jupyter |
| --- | ------- |
[![ros](https://img.shields.io/badge/ROS-Noetic-blue.svg)](http://wiki.ros.org/noetic) | ![minimal-notebook](https://img.shields.io/badge/Minimal-grey.svg) ![scipy-notebook](https://img.shields.io/badge/Scipy-grey.svg) ![datascience-notebook](https://img.shields.io/badge/Data--Science-grey.svg) ![tensorflow-notebook](https://img.shields.io/badge/Tensorflow-grey.svg)
[![ros](https://img.shields.io/badge/ROS-Foxy-blue.svg)](http://wiki.ros.org/foxy) | ![minimal-notebook](https://img.shields.io/badge/Minimal-grey.svg) ![scipy-notebook](https://img.shields.io/badge/Scipy-grey.svg) ![datascience-notebook](https://img.shields.io/badge/Data--Science-grey.svg) ![tensorflow-notebook](https://img.shields.io/badge/Tensorflow-grey.svg)
[![ros](https://img.shields.io/badge/ROS-Humble-blue.svg)](http://wiki.ros.org/humble) | ![minimal-notebook](https://img.shields.io/badge/Minimal-grey.svg) ![scipy-notebook](https://img.shields.io/badge/Scipy-grey.svg) ![datascience-notebook](https://img.shields.io/badge/Data--Science-grey.svg) ![tensorflow-notebook](https://img.shields.io/badge/Tensorflow-grey.svg)
[![ros](https://img.shields.io/badge/ROS-Rolling-blue.svg)](http://wiki.ros.org/rolling) | ![minimal-notebook](https://img.shields.io/badge/Minimal-grey.svg) ![scipy-notebook](https://img.shields.io/badge/Scipy-grey.svg) ![datascience-notebook](https://img.shields.io/badge/Data--Science-grey.svg) ![tensorflow-notebook](https://img.shields.io/badge/Tensorflow-grey.svg)

tags are formed as follows:

`<ros-version>-<notebook-type>`

where `<ros-version>` is the ROS version and `<notebook-type>` is the type of notebook. For example, `noetic-minimal` is a ROS Noetic image based on the `minimal-notebook`.

## Usage

An example `Dockerfile` for a custom notebook image:

```dockerfile
FROM ghcr.io/mpo-web-consulting/ros-notebook:noetic-minimal

# add your customizations here
USER root

RUN mamba install -y tensorflow && \
    mamba clean -y -f && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# switch back to jovyan to avoid accidental container runs as root
USER ${NB_UID}
```

## Generate Images and Actions

The images and actions are generated from templates using [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/). The templates are located in the `templates` directory. The images are defined in `images.yaml`.

Use the following commands to generate the images and github actions files:

```bash
# generate Dockerfiles for all images
python3 scripts/generate_images.py templates/Dockerfile.j2 images images.yaml

# generate actions for all images
python3 scripts/generate_workflows.py templates/action.yml.j2 images .github/workflows
```
