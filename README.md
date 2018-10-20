# Api-Mocker-Generator

[API Mocker](https://github.com/gstroup/apimocker) config and test data generator based on Swagger/OpenAPI Spec.

## Installation

```shell
$ pip install api-mocker-generator
```

## Example Usage

```
$ api-mocker-generator --swagger http://localhost:8080/api-docs
```

## Running locally

```
$ python local_main.py --swagger http://localhost:8080/api-docs
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
