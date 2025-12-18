def generate_trunk_config(intf_vlan_mapping, trunk_template):
    result_dict = {}
    for intf, vlans in intf_vlan_mapping.items():
        commands = []
        
        vlan_str = ",".join([str(v) for v in vlans])
        
        for command in trunk_template:
            if command.endswith("allowed vlan"):
                commands.append(f"{command} {vlan_str}")
            else:
                commands.append(command)
        result_dict[intf] = commands
    return result_dict
