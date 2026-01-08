def parse(feet_inches_arg):
    parts = feet_inches_arg.split(" ")
    feet_arg = float(parts[0])
    inches_arg = float(parts[1])
    return feet_arg, inches_arg
