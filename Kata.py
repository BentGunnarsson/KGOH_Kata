def Add(entry):
    if entry == "":
        return 0
    if "," not in entry and "\n" not in entry:
        return int(entry)
    entry = entry.replace("\n",",")
    entry = entry.split(",")
    ret_val = 0
    for num in entry:
        ret_val += int(num)
    return ret_val