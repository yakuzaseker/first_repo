import subprocess

def ping_ip_addresses(ip_addresses):
    reachable = []
    unreachable = []

    for ip in ip_addresses:
        reply = subprocess.run(
            ['ping', '-c', '1', '-n', ip], 
            stdout=subprocess.DEVNULL, 
            stderr=subprocess.DEVNULL
        )
        
        if reply.returncode == 0:
            reachable.append(ip)
        else:
            unreachable.append(ip)
            
    return reachable, unreachable

if __name__ == "__main__":
    ips = ["8.8.8.8", "192.168.100.200", "1.1.1.1"]
    print(ping_ip_addresses(ips))
