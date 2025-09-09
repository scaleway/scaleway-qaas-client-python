SHELL := /bin/bash

CLIENT_FOLDER=scaleway_qaas_client
OPENAPI_FOLDER=openapi

V1_ALPHA1=v1alpha1
V1_BETA1=v1beta1

define generate_client # 1: api_version
	mkdir -p ${CLIENT_FOLDER}/$(1)
	openapi-python-client generate \
	--path ${OPENAPI_FOLDER}/scaleway.qaas.$(1).Api.yml \
	--output-path ${CLIENT_FOLDER}/$(1)
	--overwrite
endef

define clean_client # api_version
	black ${CLIENT_FOLDER}/$(1)
endef

.PHONY: install
install:
	pip3 install --upgrade pip
	pip3 install openapi-python-client
	pip3 install black

.PHONY: install-test
install-test:
	pip3 install --upgrade pip
	pip3 install -r tests/requirements.txt

.PHONY: v1alpha1
v1alpha1:
	$(call generate_client,${V1_ALPHA1})

.PHONY: test
test:
	pytest -s --showprogress -vv tests/

.PHONY: clean
clean:
