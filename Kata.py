def Add(entry):
    if entry == "":
        return 0
    
    entry = entry.replace("\n",",")
    entry = entry.split(",")
    ret_val = 0
    negatives = False

    for num in entry:
        if int(num) < 0:
            negatives = True
            break
        if int(num) < 1001:
            ret_val += int(num)

    if negatives:
        neg_nums = ""
        for num in entry:
            if int(num) < 0:
                neg_nums += ","+str(num)
        neg_nums = neg_nums[1:]
        raise Exception("Negatives not allowed: "+neg_nums)

    return ret_val