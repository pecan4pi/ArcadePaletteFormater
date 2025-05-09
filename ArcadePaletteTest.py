# Open the file in read mode
file = open("palette.txt", "r")

for line in file:
    print(""" "#""" + line.strip()+ '"')  # .strip() to remove newline characters
