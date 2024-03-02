def median(arr):
    arr = sorted(arr)
    if(len(arr) == 0):
        return 0
    elif(len(arr) % 2 != 0):
        return arr[int(len(arr) / 2)]
    else:
        return (arr[int(len(arr) / 2) - 1] + arr[int(len(arr) / 2)]) / 2

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