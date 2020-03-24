def Add(entry):
    if entry == "":
        return 0
    if "," not in entry:
        return int(entry)
    entry1, entry2 = entry.split(",")
    return int(entry1) + int(entry2)