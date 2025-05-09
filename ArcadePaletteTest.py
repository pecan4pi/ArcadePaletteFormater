# Open the file in read mode
file = open("palette.txt", "r")
linenum = 1

for line in file:
    if linenum == 15: 
        print(""" "#""" + line.strip()+ '"')  # .strip() to remove newline characters

    else:
        print(""" "#""" + line.strip()+ '",')  # .strip() to remove newline characters
    
    linenum = linenum + 1
