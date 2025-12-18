from sys import argv

filename = argv[1]
with open(filename, "r") as f:
    for line in f:
        
        if not line.startswith("!") and line.strip():
            print(line.rstrip())
