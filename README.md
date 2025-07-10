# Scaleway Python client for Quantum as a Service

This Python package is basically a HTTPX client based on Pydantic over the [Quantum as a Service API](https://www.scaleway.com/en/developers/api/qaas/).

This package is intented to be used from quantum circuit SDK such as Qiskit, Cirq, Perceval and so-on.

## Installation

We encourage installing Scaleway provider via the pip tool (a Python package manager):

```bash
pip install scaleway-qaas-client
```

## Getting started

To use QaaS client, you need to have an access secret_key and a Scaleway's project_id


```python
from scaleway_qaas_client import QaaSClient

client = QaaSClient(
    project_id=os.environ["SCALEWAY_PROJECT_ID"],
    secret_key=os.environ["SCALEWAY_API_TOKEN"],
)

platforms = client.list_platforms(name="aer_simulation_pop_c16m128")

target_platform = platforms[0]

session = client.create_session(platform_id=target_platform.id, max_duration="2min", max_idle_duration="2min")

while session.status == "starting":
    session = client.get_session(session.id)
    time.sleep(3)

client.delete_session(session.id)
```

## Development
This repository is at its early stage and is still in active development. If you are looking for a way to contribute please read [CONTRIBUTING.md](CONTRIBUTING.md).

## Reach us
We love feedback. Feel free to reach us on [Scaleway Slack community](https://slack.scaleway.com/), we are waiting for you on [#opensource](https://scaleway-community.slack.com/app_redirect?channel=opensource)..

## License
[License Apache 2.0](LICENSE)
