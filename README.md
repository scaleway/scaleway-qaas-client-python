# Scaleway Pyhon client for Quantum as a Service



## Installation

We encourage installing Scaleway provider via the pip tool (a Python package manager):

```bash
pip install scaleway-qaas-client
```

## Getting started

To instantiate the ScalewayProvider, you need to have an access token and a project_id

```python
from qiskit import QuantumCircuit
from qiskit_scaleway import ScalewayProvider

provider = ScalewayProvider(
    project_id="<your-scaleway-project-id>",
    secret_key="<your-scaleway-secret-key>",
)
```

Alternatively, the Scaleway Provider can discover your access token from environment variables or from your .env file

```
export QISKIT_SCALEWAY_PROJECT_ID="project_id"
export QISKIT_SCALEWAY_API_TOKEN="token"
```

Then you can instantiate the provider without any arguments:

```python
from qiskit import QuantumCircuit
from qiskit_scaleway import ScalewayProvider

provider = ScalewayProvider()
```

Now you can have acces to the supported backends:


```python
# List all operational backends
backends = provider.backends(operational=True)
print(backends)

# List all backends with a minimum number of qbits
backends = provider.backends(min_num_qubits=35)
print(backends)

# Retrieve a backend by providing search criteria. The search must have a single match
backend = provider.get_backend("aer_simulation_h100")
```

Define a quantum circuit and run it

```python
# Define a quantum circuit that produces a 4-qubit GHZ state.
qc = QuantumCircuit(4)
qc.h(0)
qc.cx(0, 1)
qc.cx(0, 2)
qc.cx(0, 3)
qc.measure_all()

# Create and send a job to a new QPU's session (or on an existing one)
result = backend.run(qc, method="statevector", shots=1000).result()

if result.success:
    print(result.get_counts())
else:
    print(result.to_dict()["error"])

```

## Development
This repository is at its early stage and is still in active development. If you are looking for a way to contribute please read [CONTRIBUTING.md](CONTRIBUTING.md).

## Reach us
We love feedback. Feel free to reach us on [Scaleway Slack community](https://slack.scaleway.com/), we are waiting for you on [#opensource](https://scaleway-community.slack.com/app_redirect?channel=opensource)..

## License
[License Apache 2.0](LICENSE)
