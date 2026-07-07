# Network Configuration Automation Toolkit
# Step 1-5: Router, VLAN, Access Port and Trunk Configuration Generator


def generate_router_config(hostname, interface, ip, mask, description):
    return f"""
hostname {hostname}

interface {interface}
 description {description}
 ip address {ip} {mask}
 no shutdown
"""


def generate_vlan(vlan_id, vlan_name):
    return f"""
vlan {vlan_id}
 name {vlan_name}
"""


def generate_access_port(interface, vlan, description):
    return f"""
interface {interface}
 description {description}
 switchport mode access
 switchport access vlan {vlan}
"""


def generate_trunk_port(interface):
    return f"""
interface {interface}
 switchport mode trunk
"""


# Main Program

print("=== Network Configuration Automation Toolkit ===")

hostname = input("\nRouter hostname: ")
interface = input("Router interface: ")
ip = input("IP address: ")
mask = input("Subnet mask: ")
description = input("Interface description: ")


router_config = generate_router_config(
    hostname,
    interface,
    ip,
    mask,
    description
)


# VLAN Creation

vlan_config = ""

number_of_vlans = int(input("\nHow many VLANs do you want to create? "))

for i in range(number_of_vlans):
    print(f"\nVLAN {i+1}")
    
    vlan_id = input("VLAN ID: ")
    vlan_name = input("VLAN Name: ")

    vlan_config += generate_vlan(vlan_id, vlan_name)


# Access Port

access_config = ""

create_access = input("\nCreate access port? (yes/no): ")

if create_access.lower() == "yes":
    access_interface = input("Access port interface: ")
    access_vlan = input("Access VLAN ID: ")
    access_description = input("Port description: ")

    access_config = generate_access_port(
        access_interface,
        access_vlan,
        access_description
    )


# Trunk Port

trunk_config = ""

create_trunk = input("\nCreate trunk port? (yes/no): ")

if create_trunk.lower() == "yes":
    trunk_interface = input("Trunk interface: ")

    trunk_config = generate_trunk_port(
        trunk_interface
    )


# Combine everything

full_config = (
    router_config
    + vlan_config
    + access_config
    + trunk_config
)


# Save configuration

filename = f"configs/{hostname}.txt"

with open(filename, "w") as file:
    file.write(full_config)


print("\n===== GENERATED CONFIGURATION =====")
print(full_config)

print(f"\nConfiguration saved to {filename}")