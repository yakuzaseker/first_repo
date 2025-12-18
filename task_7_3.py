from sys import argv

filename = argv[1]
ignore = ["duplex", "alias", "configuration"]

with open(filename, "r") as f:
    for line in f:
        
        ignore_line = False
        for word in ignore:
            if word in line:
                ignore_line = True
        
        if not line.startswith("!") and line.strip() and not ignore_line:
            print(line.rstrip())
