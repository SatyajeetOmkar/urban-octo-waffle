def singleline_diff(line1, line2):
    if line1 == line2:
        return(-1)
    if len(line1) > len(line2):
        ranges = len(line2)
    else:
        ranges = len(line1)
    for position in range(ranges):
        if line1[position] != line2[position]:
            return(position)
    return(ranges)


def singleline_diff_format(line1, line2, idx):
    if len(line1) == len(line2) and len(line1) == 0 and idx == 0:
        return("\n^\n\n")
    positionlength = 0
    if len(line1) > len(line2):
        ranges = len(line1)
        positionlength = len(line2)
    else:
        ranges = len(line2)
        positionlength = len(line1)
    if idx > positionlength or idx < 0:
        return("")
    finalstring = ""
    str_ret = ""
    for position in range(ranges):
        if position == idx:
            finalstring += "^"
            break
        else:
            finalstring += "="
    str_ret = line1 + "\n" + finalstring + "\n"+line2 + "\n" 
    return(str_ret)
def multiline_diff(line1, line2):
    if line1 == line2:
        return((-1, -1))
    ranges = min(len(line1), len(line2))
    if line1[:ranges] == line2[:ranges]:
            return((ranges, 0))
        
    idn = -2
    for strpos in range(ranges):
        idn = singleline_diff(line1[strpos], line2[strpos])
        if idn != -2 and idn != -1:
            return((strpos, idn))

def get_file_lines(filename):
    openfile = open(filename, "rt")
    lis=[]
    for line in openfile:
        line = line.rstrip()
        lis.append(line)
    openfile.close()
    return(lis)