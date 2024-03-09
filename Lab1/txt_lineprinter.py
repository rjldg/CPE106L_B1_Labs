file_input = input("Enter file name: ")
infile = open(file_input, 'r')
lines = []

for line in infile:
    lines.append(line[:-1])
    print(line[:-1])

print(end="\n")

gatekeep_status = True
while gatekeep_status:
    line_num = int(input(f"Enter a line number (1-{len(lines)}) to retrieve the text. (0 to exit) : "))
    if line_num == 0:
        exit("Program terminated with exit code: 0")
    elif line_num > 0 and line_num <= len(lines):
        print(f"Line {line_num}: {lines[line_num-1]}")
    else:
        print("Invalid line number.")
    print(end="\n")