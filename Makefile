.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $1, $2}'

.PHONY: test
test: ## Run tests
	uv run pytest $(kata)/tests

.PHONY: create-kata
create-kata: ## Create a new kata
	@read -p "Enter the kata name: " KATA_NAME; \
	python -m scripts.create_package $$KATA_NAME
