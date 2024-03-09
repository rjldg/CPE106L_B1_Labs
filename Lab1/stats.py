def mean(arr):
    value = 0
    return value

def median(arr):
    value = 0
    return value

def mode(arr):
    value = 0
    return value

arr = list(map(int, input("Enter a list of number separated by spaces: ").split()))

stat_func_dict = {
    "mean": mean(arr),
    "median": median(arr),
    "mode": mode(arr),
}

valid_status = False
while not valid_status:
    stat_treatment = input("Enter statistical treatment to be applied (mean, median, mode) : ")
    for treatment, stat_func in stat_func_dict.items():
        if treatment == str.lower(stat_treatment):
            print(f"valid: {str.lower(stat_treatment)}")
            valid_status = True
            break
    if not valid_status:
        print("Invalid input.")
