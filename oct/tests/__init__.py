# pylint: disable=no-member
# pylint: disable=no-name-in-module
from typing import Dict, Any
from pyats import aetest
from pyats.topology import loader
from pyats.topology.testbed import Testbed


def mandatory_aetest_arguments(testbed: Testbed, device_name: str) -> Dict[str, Any]:
    return {
        "testbed": testbed,
        "grid": testbed.custom["selenium-grid"],
        "device": testbed.devices[device_name],
        "server": testbed.devices[device_name],
    }


def run_testcase(testbed_file: str = "testbed.yaml", device_name: str = "vm") -> None:
    aetest.main(**mandatory_aetest_arguments(loader.load(testbed_file), device_name))
