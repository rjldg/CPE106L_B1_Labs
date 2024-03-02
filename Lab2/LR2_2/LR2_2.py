import os.path

fn = input("Enter filename: ")
if not os.path.isfile(fn):
    exit(f"{fn} does not exists.")

infile = open(fn, 'r')
lines = []
print("\nFile contents: ")

for line in infile:
    lines.append(line[:-1])
    print(line[:-1])

print(end='\n')
print("There are {} lines in the file".format(len(lines)), '\n')
ln = int(input("Enter line number between 1-{} (0 to exit): ".format(len(lines))))

while ln != 0:
    if ln <= len(lines):
        print("\nLINE {}: ".format(ln), end="")
        print(lines[ln - 1] + "\n")

    ln = int(input("Enter line number between 1-{} (0 to exit): ".format(len(lines))))

# we push to the main, to the main, to the main, to the main, to the main, to the main, to the mai-