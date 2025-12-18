nat = "ip nat inside source list ACL interface FastEthernet0/1"
print(nat.replace("FastEthernet", "GigabitEthernet"))

mac = "AAAA:BBBB:CCCC"
print(mac.replace(":", "."))

mac = "AAAA:BBBB:CCCC"
print(mac.replace(":", "."))

vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
result = sorted(list(set(vlans)))
print(result)

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
vlan1 = set(command1.split()[-1].split(","))
vlan2 = set(command2.split()[-1].split(","))
result = sorted(list(vlan1 & vlan2))
print(result)

ospf_route = "10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
route = ospf_route.replace(",", "").replace("[", "").replace("]", "").split()
print(f"{'Prefix':25} {route[0]}")
print(f"{'AD/Metric':25} {route[1]}")
print(f"{'Next-Hop':25} {route[3]}")
print(f"{'Last update':25} {route[4]}")
print(f"{'Outbound Interface':25} {route[5]}")

mac_hex = "AAAA:BBBB:CCCC"
parts = mac_hex.split(":")
bin_mac = bin(int(parts[0], 16))[2:].zfill(16) + bin(int(parts[1], 16))[2:].zfill(16) + bin(int(parts[2], 16))[2:].zfill(16)
print(bin_mac)

ip = "192.168.3.1"
octets = ip.split(".")
print(f"{octets[0]:<10}{octets[1]:<10}{octets[2]:<10}{octets[3]:<10}")
b1 = bin(int(octets[0]))[2:].zfill(8)
b2 = bin(int(octets[1]))[2:].zfill(8)
b3 = bin(int(octets[2]))[2:].zfill(8)
b4 = bin(int(octets[3]))[2:].zfill(8)
print(f"{b1:<10}{b2:<10}{b3:<10}{b4:<10}")



