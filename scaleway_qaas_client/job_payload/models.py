# Copyright 2025 Scaleway
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

from dataclasses_json import dataclass_json


class QaaSCircuitSerializationFormat(Enum):
    UNKOWN_CIRCUIT_SERIALIZATION = 0
    QASM_V1 = 1
    QASM_V2 = 2
    QASM_V3 = 3


@dataclass_json
@dataclass
class QaaSCircuitData:
    serialization_format: QaaSCircuitSerializationFormat
    circuit_serialization: str


@dataclass_json
@dataclass
class QaaSJobRunData:
    circuits: List[QaaSCircuitData]
    options: Dict


@dataclass_json
@dataclass
class QaaSJobBackendData:
    name: str
    version: str
    options: Dict


@dataclass_json
@dataclass
class QaaSJobClientData:
    user_agent: str


@dataclass_json
@dataclass
class QaaSJobData:
    client: QaaSJobClientData
    backend: QaaSJobBackendData
    run: QaaSJobRunData
