def sort_list(num_list):
    n = len(num_list)
    i = 0
    try:
        while (i < n):
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

def print_list(list1):
    for i in range(len(list1)):
        print(list1[i])

l1 = ['a', 'c','r', 'b']

print_list(sort_list(l1))