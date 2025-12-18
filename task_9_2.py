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

def create_network_map(filenames):
    topology = {}
    for filename in filenames:
        try:
            with open(filename) as f:
                file_topology = parse_cdp_neighbors(f.read())
                topology.update(file_topology)
        except FileNotFoundError:
            continue
    return topology

if __name__ == "__main__":
    infiles = ["sh_cdp_n_sw1.txt", "sh_cdp_n_r1.txt", "sh_cdp_n_r2.txt", "sh_cdp_n_r3.txt"]
    network_map = create_network_map(infiles)
    for local, remote in network_map.items():
        print(f"{local[0]} {local[1]} -> {remote[0]} {remote[1]}")
