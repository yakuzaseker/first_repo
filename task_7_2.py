import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "config_sw1.txt"
ignore = ["duplex", "alias", "Current configuration"]

with open(filename, "r") as f:
    for line in f:
      
        line = line.rstrip()
        
        
        if not line.startswith("!"):
            
            ignore_found = False
            for word in ignore:
                if word in line:
                    ignore_found = True
            
            if not ignore_found and line:
                print(line)
