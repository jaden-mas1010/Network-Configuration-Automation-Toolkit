"""
utils.py

Utility functions for the Network Configuration Automation Toolkit.
"""
import json
from pathlib import Path
import ipaddress


def save_config(hostname: str, config: str) -> None:
    """
    Save the generated configuration to a text file.

    Args:
        hostname: Router hostname.
        config: Complete Cisco configuration.
    """

    # Create the configs directory if it doesn't exist
    config_folder = Path("configs")
    config_folder.mkdir(exist_ok=True)

    # Create the filename
    filename = config_folder / f"{hostname}.txt"

    # Write the configuration to the file
    with open(filename, "w") as file:
        file.write(config)

    print(f"\nConfiguration saved to {filename}")


def validate_ip(ip: str) -> bool:
    """
    Validate an IPv4 or IPv6 address.

    Args:
        ip: IP address entered by the user.

    Returns:
        True if the IP address is valid, otherwise False.
    """

    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def validate_vlan(vlan_id: int) -> bool:
    """
    Validate a VLAN ID.

    Valid VLAN range:
    1 - 4094
    """

    return 1 <= vlan_id <= 4094
def validate_subnet_mask(mask: str) -> bool:
    """
    Validate a subnet mask.
    """

    try:
        ipaddress.IPv4Network(f"0.0.0.0/{mask}")
        return True
    except ValueError:
        return False
def load_json(filename: str) -> dict:
 

    with open(filename, "r") as file:
        return json.load(file)