```shell
# Adding dependencies
$ poetry add rasterio geopandas
$ poetry add --group=dev pytest coverage loguru

# Example Usage
$ poetry run project 10.0 20.0

# Testing
$ coverage run -m pytest project/
$ coverage report
```
