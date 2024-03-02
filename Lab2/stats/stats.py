from mode import mode
from mean import mean
from median import median

l = list(map(int, input("Enter list: ").split()))
n = int(input("Enter 1 to get MEAN, 2 to get MEDIAN, 3 to get MODE: "))

print(*l)

l = [] if len(l) == 0 else l

funcs = {
    1: mean(l),
    2: median(l),
    3: mode(l)
}

for index, func in funcs.items():
    if(index == n):
        if isinstance(func, list):
            print("Multiple Modes:", func)
        else:
            print(f"Ans: {func:.2f}")