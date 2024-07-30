# function app name to deploy
FUNCTION_APP_NAME := die-webapi

.PHONY: help
help: ## print this message ## make
	@echo "publish to $(FUNCTION_APP_NAME)"
	@printf "\033[36m%-30s\033[0m %-50s %s\n" "[Sub command]" "[Description]" "[Example]"
	@grep -E '^[/a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | perl -pe 's%^([/a-zA-Z_-]+):.*?(##)%$$1 $$2%' | awk -F " *?## *?" '{printf "\033[36m%-30s\033[0m %-50s %s\n", $$1, $$2, $$3}'

.PHONY: clean
clean: ## clean the function app ## make clean
	func azure functionapp publish $(FUNCTION_APP_NAME) --nozip

.PHONY: publish
publish: ## publish to the function app ## make publish
	func azure functionapp publish $(FUNCTION_APP_NAME)
