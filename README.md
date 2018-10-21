# Api-Mocker-Generator

[![Maintainability](https://api.codeclimate.com/v1/badges/c221df53ac279d0b767f/maintainability)](https://codeclimate.com/github/namuan/api-mocker-generator/maintainability)
[![CircleCI](https://circleci.com/gh/namuan/fuzzy-swagger.svg?style=svg)](https://circleci.com/gh/namuan/fuzzy-swagger)

[API Mocker](https://github.com/gstroup/apimocker) config and test data generator based on Swagger/OpenAPI Spec.

## Installation

```shell
$ pip install api-mocker-generator
```

## Usage

```
usage: local_main.py [-h] --swagger SWAGGER --output OUTPUT [--verbose]

optional arguments:
  -h, --help         show this help message and exit
  --swagger SWAGGER  Location of swagger document. Could be HTTP endpoint or
                     local file system
  --output OUTPUT    Output directory for configuration and mocked responses
  --verbose
```

Example command

```
$ api-mocker-generator --swagger http://localhost:8080/api-docs --output ./out
```

## Running locally during development

```
$ python local_main.py --swagger http://localhost:8080/api-docs --output ./out
```

## Verbose debugging

To turn on verbose output for debugging, set the `--verbose` argument.

## Publishing Updates to PyPi

For the maintainer, increment the version number in api_mocker_generator.py and run the following:

```shell
docker build -f ./Dockerfile.buildenv -t namuan/api_mocker_generator:build .
docker run --rm -it --entrypoint python namuan/api_mocker_generator:build setup.py publish
```

Enter the username and password for pypi.org repo when prompted
