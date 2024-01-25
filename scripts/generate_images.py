#!/usr/bin/env python3

"""
generate_images.py

Generate Dockerfiles for Jupyter ROS images

Usage:
    generate_images.py <template> <output_dir> <images>
"""

import os
from argparse import ArgumentParser
from jinja2 import Environment, FileSystemLoader
import yaml


# main
if __name__ == '__main__':
    parser = ArgumentParser(
        description='Generate Dockerfiles for Jupyter ROS images')
    # required arguments
    parser.add_argument(
        'template', default='templates/Dockerfile.j2', help='Template file')
    parser.add_argument('output_dir', default='images',
                        help='Output directory')
    parser.add_argument('images', default='images.yaml', help='Images file')

    # optional arguments
    args = parser.parse_args()

    # Load templates from the current directory
    env = Environment(loader=FileSystemLoader(os.path.dirname(args.template)))
    template = env.get_template(os.path.basename(args.template))

    # load the images file
    with open(args.images, 'r') as f:
        images = yaml.safe_load(f)

    # generate and save the generated Dockerfiles for each image
    for im in images['base_notebook_images']:
        for flavour in images['ros_flavours']:
            # create the output directory if it doesn't exist
            dir = os.path.join(args.output_dir, im.removeprefix(
                'jupyter/').removesuffix('-notebook'), flavour['ros_distro'])
            os.makedirs(dir, exist_ok=True)

            # variables to substitute in the template
            vars = {
                'TEMPLATE_BASE_IMAGE': im + ':' + flavour['notebook_tag'],
                'TEMPLATE_ROS_VERSION': flavour['ros_distro'],
                'TEMPLATE_ROS_GENERATION': 'ros{}'.format(flavour['ros_version']),
                'TEMPLATE_ROS_REPO_KEY': 'C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654',
                'TEMPLATE_UBUNTU_CODENAME': flavour['ubuntu_codename'],
            }

            # render the template with the variables
            dockerfile = template.render(vars)

            # save the generated Dockerfile
            with open(os.path.join(dir, 'Dockerfile'), 'w') as f:
                f.write(dockerfile)
