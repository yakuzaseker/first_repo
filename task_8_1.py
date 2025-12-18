def generate_access_config(intf_vlan_mapping, access_template):
    result = []
    for intf, vlan in intf_vlan_mapping.items():
        result.append(f"interface {intf}")
        for command in access_template:
            if command.endswith("access vlan"):
                result.append(f"{command} {vlan}")
            else:
                result.append(command)
    return result


access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]
access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11}

print(generate_access_config(access_config, access_mode_template))
