.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $1, $2}'

.PHONY: test
test:
	pdm run pytest $(kata)/tests

.PHONY: create-package
create-package:
	@read -p "Enter the kata name: " PACKAGE_NAME; \
	python -m scripts.create_package $$PACKAGE_NAME
