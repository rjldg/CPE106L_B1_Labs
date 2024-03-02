fn = input("Enter filename: ")

infile = open(fn, 'r')

lines = []


print("\nFile contents: ")

for line in infile:
        lines.append(line[:-1])
        print(line[:-1])
print(end='\n')

ln = int(input("Enter line number (0 to exit): "))

while ln != 0:

    if ln <= 9:
        print("\nLine contents: ")

        print(lines[ln - 1] + "\n")

    ln = int(input("Enter line number (0 to exit): "))
