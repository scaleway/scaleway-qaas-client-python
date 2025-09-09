SHELL := /bin/bash

CLIENT_FOLDER=scaleway_qaas_client
OPENAPI_FOLDER=openapi

V1_ALPHA1=v1alpha1
V1_BETA1=v1beta1

define generate_client # 1: api_version
	mkdir -p ${CLIENT_FOLDER}/$(1)
	openapi-python-client generate \
	--path ${OPENAPI_FOLDER}/scaleway.qaas.$(1).Api.yml \
	--output-path ${CLIENT_FOLDER}/$(1) \
	--overwrite \
	--no-fail-on-warning || true
endef

define clean_client # api_version
	rm ${CLIENT_FOLDER}/$(1)/.gitignore
	rm ${CLIENT_FOLDER}/$(1)/pyproject.toml
	rm ${CLIENT_FOLDER}/$(1)/README.md
	black ${CLIENT_FOLDER}/$(1)
endef

.PHONY: install
install:
	pip3 install --upgrade pip
	pip3 install openapi-python-client
	pip3 install black

.PHONY: v1alpha1
v1alpha1:
	$(call generate_client,${V1_ALPHA1})
	$(call clean_client,${V1_ALPHA1})

.PHONY: install-test
install-test:
	pip3 install --upgrade pip
	pip3 install -r tests/requirements.txt

.PHONY: test
test:
	pytest -s --showprogress -vv tests/