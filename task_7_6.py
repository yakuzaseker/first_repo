result = []
with open("CAM_table.txt", "r") as f:
    for line in f:
        parts = line.split()
        if parts and parts[0].isdigit():
            vlan, mac, _, intf = parts
            
            result.append([int(vlan), mac, intf])

for vlan, mac, intf in sorted(result):
    print(f"{vlan:<10} {mac:20} {intf}")
