def mean(arr):
    value = 0
    for num in arr:
        value += num
    return '{0:.2f}'.format((value/len(arr)))

def median(arr):
    arr = sorted(arr)
    if len(arr) % 2 == 1:
        value = arr[int((len(arr)-1)/2)]
    else:
        value = (arr[int((len(arr))/2)] + arr[int((len(arr)/2) - 1)])/2
    return '{0:.2f}'.format(value)

def mode(arr):
    num_frequency = {}

    # sort frequency
    for num in arr:
        exist_status = False
        if len(num_frequency) > 0:
            for key, v in num_frequency.items():
                if num == key:
                    num_frequency.update({key: v+1})
                    exist_status = True
                    break
        if not exist_status:
            num_frequency.update({num: 1})

    # get max frequency
    value = []
    max_freq = 1
    for key, v in num_frequency.items():
        if v > max_freq:
            max_freq = v
            value = [key]
        elif v == max_freq and v != 1:
            value.append(key)

    if len(value) == 0:
        value = "N/A"
    else:
        value = ', '.join(str(result) for result in value)
    
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
            print(f"The {str.lower(stat_treatment)} of the given list is: {stat_func}")
            valid_status = True
            break
    if not valid_status:
        print("Invalid input.")
