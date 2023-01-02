import sys
import re

lines = [line.rstrip("\n\r()") for line in sys.stdin.readlines()]

for line in lines:
    operation, obj, string = line.split(";")
    
    if operation == "S":
        string = re.sub(r"(\w)([A-Z])", r"\1 \2", string).lower()
    
    else:
        string = string.title().replace(" ", "")
        if obj == "M":
            string += "()"
        if obj != "C":
            string = string[0].lower() + string[1:]
    
    print(string)
