
# ---- LISTS ---- 


# Getting input for different no of elements 
print("Enter elements in list : " , end = "" )
nums = list(map(int , input().split()))
print(nums, type(nums))



# Getting input for n elements
'''
n = int(input("Enter no of elements in list : "))
nums = []
for i in range(n) :
    print("Enter element at ", i , " : ", end = " ")
    num = int(input())
    nums.append(num)
print(nums, type(nums), type(nums[0]))
'''




# ---- LISTS ----

"""
# ---- Functions ----
def c() :
    print("inside c")

def b() :
    c() 
    print("inside b")

def a() :
    b() 
    print("inside a")
    c() 

a() 
print("inside main")
c()
# ---- Functions ----
"""




"""
n = int(input("Enter n : "))
# Number pattern 
k = (2 * n) - 1 
for i in range(k) :
    for j in range(k) :
        # Find all 4 borders
        top = i
        left = j 
        right = k - 1 - j
        down = k - 1 - i 
        num = min(top, left, right, down) 
        print(n - num , end = " ")
    print()
"""
'''
# Number pattern 
end = (2 * n) - 1
for i in range(n) :
    num = (2 * i) + 1
    for j in range(n) :
        print(num, end = " ")
        num += 2 
        if num > end :
            num = 1
    print()
'''

'''
# Diamond pattern 
# First half
for i in range(1, n + 1) : 
    # Spaces -> n - i
    for j in range(1, n - i + 1):
        print("_", end = " ")
    # Stars -> 2 * i - 1
    for j in range(1, 2 * i) :
        print("*", end = " ")
    print()
# Second half
for i in range(n - 1, 0, -1) : 
    # Spaces -> n - i
    for j in range(1, n - i + 1):
        print("_", end = " ")
    # Stars -> 2 * i - 1
    for j in range(1, 2 * i) :
        print("*", end = " ")
    print()
'''


'''
# Square pattern
for i in range(1, n + 1) :
    # Spaces -> n - i
    for j in range(1, n - i + 1) :
        print("_", end = " ")
    # Stars -> i
    for j in range(1, i + 1) :
        print("*", end = " ")
    print()
'''


# Multiplication table

# for i in range(1, 11) :
#     print(i , "*", n , " = ", (n * i))


# for i in range(1, n, 2) :
#     print(i, end = " ")


'''
n = int(input("Enter n : "))
if n % 3 == 0 and n % 5 == 0 :
    print('Divisible by 3 and 5')
elif n % 3 == 0 :
    print('Divisible by 3')
elif n % 5 == 0 :
    print('Divisible by 5')
else : 
    print('Not Divisible by 3 and 5')
print('In line 10')
'''


# n = 2 ^ 5
# print(n, type(n))

# n = int(input("Enter n : "))
# print(n, type(n))

# print("Hello", n, end = " ")
