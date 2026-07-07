
"""
router.py

Contains functions for generating Cisco router configurations.
"""


def generate_router_config(
    hostname: str,
    interface: str,
    ip: str,
    mask: str,
    description: str,
) -> str:
    """
    Generate a basic Cisco router interface configuration.
    """

    return f"""hostname {hostname}

interface {interface}
 description {description}
 ip address {ip} {mask}
 no shutdown
"""
def generate_static_route(
    destination: str,
    mask: str,
    next_hop: str,
) -> str:
    """
    Generate a Cisco static route.

    Args:
        destination: Destination network.
        mask: Subnet mask.
        next_hop: Next-hop IP address.

    Returns:
        Cisco static route configuration.
    """

    return (
        f"ip route {destination} "
        f"{mask} "
        f"{next_hop}\n"
    )


def generate_default_route(next_hop: str) -> str:
    """
    Generate a Cisco default route.

    Args:
        next_hop: Gateway IP.

    Returns:
        Cisco default route.
    """

    return f"ip route 0.0.0.0 0.0.0.0 {next_hop}\n"


def generate_ospf(
    process_id: int,
    network: str,
    wildcard: str,
    area: int,
) -> str:
    """
    Generate a basic OSPF configuration.
    """

    return (
        f"router ospf {process_id}\n"
        f" network {network} {wildcard} area {area}\n"
    )