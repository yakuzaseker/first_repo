vlan_input = input("Enter VLAN number: ")

with open("CAM_table.txt", "r") as f:
    for line in f:
        parts = line.split()
        if parts and parts[0] == vlan_input:
            vlan, mac, _, intf = parts
            print(f"{vlan:<10} {mac:20} {intf}")
