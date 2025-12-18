def generate_access_config(intf_vlan_mapping, access_template, psecurity=None):
    result = []
    for intf, vlan in intf_vlan_mapping.items():
        result.append(f"interface {intf}")
        for command in access_template:
            if command.endswith("access vlan"):
                result.append(f"{command} {vlan}")
            else:
                result.append(command)
        
        
        if psecurity:
            for cmd in psecurity:
                result.append(cmd)
    return result0
