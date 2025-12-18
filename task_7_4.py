from sys import argv

src_file, dst_file = argv[1], argv[2]
ignore = ["duplex", "alias", "configuration"]

with open(src_file, "r") as src, open(dst_file, "w") as dst:
    for line in src:
        ignore_line = False
        for word in ignore:
            if word in line:
                ignore_line = True
        
        if not line.startswith("!") and line.strip() and not ignore_line:
            dst.write(line)
