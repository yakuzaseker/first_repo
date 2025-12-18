import sys

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    result = []
    for intf, vlans in intf_vlan_mapping.items():
        result.append(f"interface {intf}")
        for command in trunk_template:
            if command.endswith("allowed vlan"):
                vlan_str = ",".join([str(v) for v in vlans])
                result.append(f"{command} {vlan_str}")
            else:
                result.append(command)
    return result

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]
}

final_config = generate_trunk_config(trunk_config, trunk_template)

for line in final_config:
    print(line)
