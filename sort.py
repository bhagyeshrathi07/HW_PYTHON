def sort_list(num_list):
    n = len(num_list)
    i = 0
    try:
        while (i < n):
            if (type(num_list[i]) == int):
                j = 0
                while (j < n - i - 1) :
                    if (num_list[j] > num_list[j+1]):
                        tmp = num_list[j]
                        num_list[j] = num_list[j+1]
                        num_list[j+1] = tmp
                    j += 1
                i += 1    
        return num_list
    except:
        print("Invalid Input")

l1 = [2, 8, 4, 3, 9, 57, 1, 0, 23, 36, 82]
print(sort_list(l1))