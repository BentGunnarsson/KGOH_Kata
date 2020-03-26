def Add(entry):
    if entry == "":
        return 0

    if entry[:2] == "//":
        # Adding a new delimiter
        delim = entry[2]
        entry = entry[4:]
        entry = entry.replace(delim,",")

    entry = entry.replace("\n",",")

    entry = entry.split(",")

    ret_val = 0
    negatives = False
    neg_nums = ""

    for num in entry:
        if int(num) < 0:
            negatives = True
            neg_nums += ","+str(num)
            
        if int(num) < 1001:
            ret_val += int(num)

    if negatives:
        neg_nums = neg_nums[1:]
        raise Exception("Negatives not allowed: "+neg_nums)

    return ret_val
