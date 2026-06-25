

# Getting input for a matrix where number of rows and no of cols are different 

matrix = [] 
rows = int(input("Enter no of rows : "))

for i in range(rows) :
    print("Enter elements at ", i , " row : " , end = " ")
    nums = list(map(int, input().split()))
    matrix.append(nums)



# Getting input for a matrix where number of rows and cols are known

# matrix = []
# rows = int(input("Enter no of rows : "))
# cols = int(input("Enter no of cols : "))

# for i in range(rows) :
#     nums = [] 
#     for j in range(cols) :
#         print("Enter element at ", i, j, " : ", end = " ")
#         num = int(input())
#         nums.append(num)
#     matrix.append(nums)


# Accessing the matrix via for each loop 

# for row in matrix :
#     for elem in row :
#         print(elem, end = " ")
#     print()


# Accessing the matrix via index 

for i in range(len(matrix)) :
    print(i, " row elements : ", end = "")
    for j in range(len(matrix[i])) :
        print(matrix[i][j] , end = " ")
    print()

# print(matrix, type(matrix))