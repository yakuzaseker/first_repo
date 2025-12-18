ip_address = input("Введите IP-адрес: ")
first_byte = int(ip_address.split(".")[0])

if ip_address == "255.255.255.255":
    print("local broadcast")
elif ip_address == "0.0.0.0":
    print("unassigned")
elif 1 <= first_byte <= 223:
    print("unicast")
elif 224 <= first_byte <= 239:
    print("multicast")
else:
    print("unused")
