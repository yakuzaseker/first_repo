from task_10_1 import ping_ip_addresses
from task_10_2 import convert_ranges_to_ip_list

def print_ip_table(reachable, unreachable):
    print(f"{'Reachable':<20} {'Unreachable':<20}")
    print(f"{'-'*20} {'-'*20}")
    
    max_len = max(len(reachable), len(unreachable))
    
    for i in range(max_len):
        r = reachable[i] if i < len(reachable) else ""
        u = unreachable[i] if i < len(unreachable) else ""
        print(f"{r:<20} {u:<20}")

if __name__ == "__main__":
    ip_list = ['8.8.8.8', '192.168.100.1-2']
    converted_ips = convert_ranges_to_ip_list(ip_list)
    reach, unreach = ping_ip_addresses(converted_ips)
    print_ip_table(reach, unreach)
