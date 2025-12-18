def convert_ranges_to_ip_list(ip_list):
    result_ips = []
    for item in ip_list:
        if "-" in item:
            start_ip, stop_part = item.split("-")
            octets = start_ip.split(".")
            start_octet = int(octets[-1])
            
            if "." in stop_part:
                stop_octet = int(stop_part.split(".")[-1])
            else:
                stop_octet = int(stop_part)
            
            for i in range(start_octet, stop_octet + 1):
                octets[-1] = str(i)
                result_ips.append(".".join(octets))
        else:
            result_ips.append(item)
    return result_ips

if __name__ == "__main__":
    test_list = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    print(convert_ranges_to_ip_list(test_list))
