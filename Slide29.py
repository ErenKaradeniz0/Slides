data = [[1, 2, 3], [4, 5, 6]]
for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j])

grid = [[8, 2, 7, 8, 2, 1], [1, 5, 1, 7, 4, 7],
        [5, 9, 60, 7, 3, 2], [7, 8, 7, 7, 7, 9],
        [4, 2, 6, 9, 2, 3], [2, 2, 80, 1, 1, 3]]
def mystery(data, pos,n):
    result=[]
    j =0
    while(j<=n):
        result.append(data[pos][j])
        j+=1
    return result

print(mystery(grid,4,2))

def max_row(list_of_list):
    max=0
    for i in range(len(list_of_list)):
        for j in range(len(list_of_list[i])):
            if max<list_of_list[i][j]:
                max=list_of_list[i][j]
    return max

print(max_row(grid))

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def swap(list,index1,index2):
    for i in range(len(list)):
        temp=list[i][index1-1]
        list[i][index1-1]=list[i][index2-1]
        list[i][index2-1]=temp
    return list

print(swap(data,2,3))

#[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
def create_matrix(width,height):
    arr=[]
    for i in range(height): # 0 1 2
        arr.append([0]*width)
        for j in range(width): # 0 1 2 3 4
            arr[i][j]=j
    return arr

print(create_matrix(3,3))


#mountain peak
