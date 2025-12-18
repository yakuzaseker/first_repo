from sys import argv

if len(argv) > 1:
    filename = argv[1]
else:
    filename = "config_sw1.txt"

ignore = ["duplex", "alias", "configuration"]
ignore = ["duplex", "alias", "configuration"]

with open(filename, "r") as f:
    for line in f:
        
        ignore_line = False
        for word in ignore:
            if word in line:
                ignore_line = True
        
        if not line.startswith("!") and line.strip() and not ignore_line:
            print(line.rstrip())
