list_temp = [1, 1]
num_rows = int(input("Please Inter Numbers: "))
print([1])
print(list_temp)
for j in range(num_rows - 2):
    list = [1]
    for i in range(1, len(list_temp)):
        list.append(list_temp[i - 1] + list_temp[i])
    list.append(1)
    list_temp = list.copy()
    list.clear()
    print(list_temp)