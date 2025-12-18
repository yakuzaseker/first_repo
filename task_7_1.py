with open("ospf.txt", "r") as f:
    for line in f:
      
        route = line.replace(",", "").replace("[", "").replace("]", "").split()
        print(f"{'Prefix':25} {route[0]}")
        print(f"{'AD/Metric':25} {route[1]}")
        print(f"{'Next-Hop':25} {route[3]}")
        print(f"{'Last update':25} {route[4]}")
        print(f"{'Outbound Interface':25} {route[5]}\n")
