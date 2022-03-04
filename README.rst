
Basin information - microservice
================================

🧰 About - Usage
-----------------

Developed by Shd at SMHI.

- Python based service using Flask
- Get water body information based on a given point (latitude and longitude).
- `Microservice Template <https://github.com/shark-microservices/microservice_template>`_
- Get the latest version of the `shapefile <https://www.smhi.se/data/hydrologi/sjoar-och-vattendrag/ladda-ner-data-fran-svenskt-vattenarkiv-1.20127>`_ used in this repo


💻 Installation - Getting started
----------------------------------

When using GDAL related python packages (eg. geopandas) we find that a conda
environment is the best option for installation. Start by installing miniconda
on your system and then:

Create environment:

.. code-block:: bash

    conda env create --file environment.yaml

Activate environment:

.. code-block:: bash

    conda activate py38

Run microservice:

.. code-block:: bash

    python app.py