# Scaleway Pyhon client for Quantum as a Service



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

assert platforms is not None
assert len(platforms) == 1

target_platform = platforms[0]

assert target_platform.id is not None

session = client.create_session(platform_id=target_platform.id, max_duration="2min", max_idle_duration="2min")

assert session is not None
assert session.id is not None
assert session.platform_id == target_platform.id

while session.status == "starting":
    session = client.get_session(session.id)
    time.sleep(3)

assert session.status == "running"

client.delete_session(session.id)
```

## Development
This repository is at its early stage and is still in active development. If you are looking for a way to contribute please read [CONTRIBUTING.md](CONTRIBUTING.md).

## Reach us
We love feedback. Feel free to reach us on [Scaleway Slack community](https://slack.scaleway.com/), we are waiting for you on [#opensource](https://scaleway-community.slack.com/app_redirect?channel=opensource)..

## License
[License Apache 2.0](LICENSE)
