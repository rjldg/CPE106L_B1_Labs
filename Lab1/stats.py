def mode(l):
    print(max(set(l), key=l.count))

def mean(l):
    print("lorem ipsum")

def median(l):
    print("lorem ipsum")

l = list(map(int, input("Enter list: ").split()))
n = int(input("Enter 1 to get MODE, 2 to get MEAN, 3 to get MEDIAN: "))

print(*l)

funcs = {
    1: mode(l),
    2: mean(l),
    3: median(l)
}

for index, func in funcs.items():
    if(index == n):
        if(func == -1):
            print("No Mode.")
        else:
            print(f"Ans: {func:.2f}")