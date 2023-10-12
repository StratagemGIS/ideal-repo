# Tech Stack

## `Miniconda` for Python Environment Management
https://docs.conda.io/projects/miniconda
- Miniconda allows you to create and manage isolated Python environments with specific Python versions.
- You can easily switch between different Python versions and avoid conflicts between projects that require different Python versions.
- Conda also handles system-level dependencies, which can be essential for some scientific and data science libraries.

## `Poetry` for Project Dependency Management
https://python-poetry.org
- Poetry is a modern Python packaging and dependency management tool designed to simplify the management of project-specific dependencies.
- It provides a clear and standardized way to declare project dependencies in a pyproject.toml file, making it easier to share and reproduce project environments.
- Using Poetry within a Conda environment allows you to create isolated environments for your Python projects.
  This means you can manage project-specific dependencies using Poetry while still benefiting from Conda's isolation and system-level dependency management.

## `Rasterio`, `Geopandas` for Geospatial Data Management
https://rasterio.readthedocs.io, https://geopandas.org
- Rasterio is a Python library for reading and writing geospatial raster data. It simplifies the manipulation of raster datasets, such as satellite imagery.
- Geopandas is a Python library for working with geospatial vector data. It simplifies the manipulation and analysis of geographic information in the form of vector datasets (e.g., shapefiles, GeoJSON, and other formats).

## `Pytest`, `Coverage`, `Loguru` for Testing and Logging
https://pytest.org, https://coverage.readthedocs.io, https://loguru.readthedocs.io
- Pytest is a testing framework for Python that simplifies the process of writing and executing unit tests and functional tests.
- Coverage is a tool for measuring code coverage in your Python applications. It helps you identify which parts of your codebase are covered by tests and which are not.
- Loguru is a Python logging library designed to make logging simpler, more flexible, and more user-friendly.
