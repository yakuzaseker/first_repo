def parse_cdp_neighbors(command_output):
    result = {}
    lines = command_output.strip().split("\n")
    hostname = lines[0].split(">")[0]
    
    for line in lines:
        parts = line.split()
        if len(parts) > 4 and parts[3].isdigit():
            neighbor = parts[0]
            local_int = parts[1] + parts[2]
            remote_int = parts[-2] + parts[-1]
            result[(hostname, local_int)] = (neighbor, remote_int)
            
    return result

if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        topology = parse_cdp_neighbors(f.read())
        for local, remote in topology.items():
            print(f"{local[0]} {local[1]} -> {remote[0]} {remote[1]}")
