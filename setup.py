# Copyright (c) 2021 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE or http://opensource.org/licenses/mit).
"""
Created on 2021-02-18 13:52

@author: johannes
"""
import os
import setuptools


requirements = []
with open('requirements.txt', 'r') as fh:
    for line in fh:
        requirements.append(line.strip())

with open('README.rst', 'r') as file:
    README = file.read()

NAME = 'microservice_point_basin_info'

setuptools.setup(
    name=NAME,
    version="0.1.1",
    author="SMHI - NODC",
    author_email="shark@smhi.se",
    description="Get water body information based on a given point",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/shark-microservices/microservice_point_basin_info",
    packages=setuptools.find_packages(),
    package_data={'microservice_point_basin_info': [
        os.path.join('water_bodies', 'resources', '*.cpg'),
        os.path.join('water_bodies', 'resources', '*.dbf'),
        os.path.join('water_bodies', 'resources', '*.prj'),
        os.path.join('water_bodies', 'resources', '*.shp'),
        os.path.join('water_bodies', 'resources', '*.shx'),
        os.path.join('*.yaml'),
    ]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=requirements,
)
