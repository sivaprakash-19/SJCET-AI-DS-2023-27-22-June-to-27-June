
# ---- DICTIONARY ---- 

nums = {
    49 : 3
} 

nums.pop(490, print("Not found")) # Removes the key value pair from dict, if key is not present -> Throw KeyError, but if 2nd argument is present -> Returns the 2nd argument. T.C -> O(1)

# print(nums.get(490)) # Returns the value if key is present, if key not present -> Returns None. T.C -> O(1)

# nums[4] = 5 # Check whether key value pair exists -> update value of key, if key is not present -> create a new key value pair into dictionary. T.C -> O(1)

print(nums, type(nums))









# ---- DICTIONARY ---- 


# ---- SET ---- 

# nums = {19, 20, 10, 10}

# # Checking if element is present in set. T.C -> O(1)
# if 10 in nums :
#     print("present") 
# else :
#     print("not present")

# nums.add(3) # Adds element to set, if element is present -> ignore. T.C -> O(1)

# nums.remove(190) # Removes the element from set, if element is not present -> Throws KeyError. T.C -> O(1)

# nums.discard(190) # Removes the element from set, if element is not present -> ignore. T.C -> O(1)

# print(nums , type(nums))


# ---- SET ---- 

# ---- LISTS ---- 

# nums = [101, 20, 1, 24, 45, 67, 10]

# nums.reverse()  # Reverses the list. 

# nums.sort() # Sort the list -> T.C -> O(n logn)

# nums.pop() # Removes the element at last index, if list is empty -> Throw IndexError -> T.C -> O(1)

# print(nums)

# nums.clear() # Removes all elements from list. T.C -> O(1)

# nums.insert(560, 8) # Inserts the element at a specific index, if index is not valid -> Insert at last. T.C -> O(n)

# nums.append(90) # Appends element to the last in list. T.C -> O(1)

# print(nums, type(nums))

# Checking if an element is present in list. T.C -> O(n)
# if 100 in nums :
#     print("present")
# else :
#     print("not present")

# try :
#     print(nums.index(100))
# except(ValueError) :
#     print("Element not present")

# print(nums.index(100)) # Returns the first occurrence of the element, if not present -> Throw ValueError. T.C -> O(n)

# print(nums.count(101)) # Returns the number of occurrences of an element. T.C -> O(n)



# Getting input for different no of elements 

# nums = input().split()  # List of words
# print(nums)
# print("Enter elements in list : " , end = "" )
# nums = list(map(int , input().split('ab')))
# print(nums, type(nums))

'''
input() -> get input as string
input().split() -> convert into a list of strings, sep -> ' ' 
map(int, input().split()) -> Iterate through the list of words and convert each element into a int
list(map(int, input().split())) -> Store all integers in list
'''


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