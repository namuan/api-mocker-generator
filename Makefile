export PROJECTNAME=$(shell basename "$(PWD)")

.SILENT: ;               # no need for @

clean: ## Cleans all cached files
	find . -type d -name '__pycache__' | xargs rm -rf
	find . -type f -name '*.pyc' -exec rm -rf {} +

build-docker: ## Builds Docker image for building PyPi release
	docker build -f ./Dockerfile.buildenv -t namuan/api_mocker_generator:build .

publish: clean ## Publishes release to PyPi
	docker run --rm -it --entrypoint python namuan/api_mocker_generator:build setup.py publish

.PHONY: help
.DEFAULT_GOAL := help

help: Makefile
	echo
	echo " Choose a command run in "$(PROJECTNAME)":"
	echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	echo
