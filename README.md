# Python client for Scaleway's Quantum as a Service

This Python package is basically a HTTPX client based on Pydantic over the [Quantum as a Service API](https://www.scaleway.com/en/developers/api/qaas/).

This package is intented to be used from quantum circuit SDK such as Qiskit, Cirq, Perceval and so-on.

## Installation

We encourage installing this package via the pip tool (a Python package manager):

```bash
pip install scaleway-qaas-client
```

## Getting started

To use the client, you need to have an access secret_key and a Scaleway's project_id

```python
from scaleway_qaas_client import QaaSClient

client = QaaSClient(
    project_id=os.environ["SCALEWAY_PROJECT_ID"], # Your project ID in UUID format
    secret_key=os.environ["SCALEWAY_SECRET_KEY"], # Your personal secret key in UUID format
)

platforms = client.list_platforms(name="aer_simulation_pop_c16m128")

target_platform = platforms[0]

session = client.create_session(platform_id=target_platform.id, max_duration="2min", max_idle_duration="2min")

while session.status == "starting":
    session = client.get_session(session.id)
    time.sleep(3)

client.delete_session(session.id)
```

## Development and contribution
This repository is at its early stage and is still in active development. If you are looking for a way to contribute please read [CONTRIBUTING.md](CONTRIBUTING.md).

### Install dev package
To install necessary packages for contribution development, please install via:

```bash
make install
```

### Code generation
We use open API format (in [openapi/ folder](openapi)) and generate client version manually.

Here how to generate the `v1alpha1` version:

```bash
make v1alpha1
```

## Reach us
We love feedback. Feel free to reach us on [Scaleway Slack community](https://slack.scaleway.com/), we are waiting for you on [#opensource](https://scaleway-community.slack.com/app_redirect?channel=opensource)..

## License
[License Apache 2.0](LICENSE)
