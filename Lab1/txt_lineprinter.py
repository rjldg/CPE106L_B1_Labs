fn = input("Enter filename: ")

infile = open(fn, 'r')

lines = []

print("\nFile contents: ")
for line in infile:
    print(line[:-1])
    lines.append(line[:-1])

ln = int(input("Enter line number (0 to exit): "))

while ln != 0:

    print(lines[ln - 1])

    ln = int(input("Enter line number (0 to exit): "))
