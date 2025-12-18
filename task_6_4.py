while True:
    ip_address = input("Введите IP-адрес: ")
    octets = ip_address.split(".")
    valid_ip = True

    if len(octets) == 4:
        for octet in octets:
            if not (octet.isdigit() and 0 <= int(octet) <= 255):
                valid_ip = False
                break
    else:
        valid_ip = False

    if valid_ip:
       
        first_byte = int(octets[0])
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
        break
    else:
        print("Неправильный IP-адрес")
