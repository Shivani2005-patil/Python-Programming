# Check if a Key Exists in a Dictionary
# def check_key(data_dict, key):
#     if key in data_dict:
#         return "Key Exists"
#     else:
#         return "Key Not Found"
# # Sample Input
# data_dict = {"name": "Alice", "age": 30}
# print(check_key(data_dict, "age")) # Output: Key Exists


#Iterate Over Dictionary Keys and Values
# def iterate_dict(data_dict):
#     for key, value in data_dict.items():
#         print(f"Key: {key}, Value: {value}")

# # Sample Input
# data_dict = {"name": "Alice", "age": 30}
# iterate_dict(data_dict)


#Merge Two Dictionaries
# def merge_dicts(dict1, dict2):
#     # This creates a new dictionary by unpacking both
#     merged = {**dict1, **dict2}
#     return merged

# # Sample Input
# d1 = {"name": "Alice"}
# d2 = {"age": 30}
# print(merge_dicts(d1, d2)) # Output: {'name': 'Alice', 'age': 30}

#Reverse a String
# def reverse_string(text):
#     reversed_text = ""
#     for char in text:
#         # Add the character to the FRONT of the new string
#         reversed_text = char + reversed_text
#     return reversed_text

# # Sample Input
# print(reverse_string("hello")) # Output: "olleh"

# Check for Palindrome
# def is_palindrome(text):
#     # Standardize to lowercase to avoid case-sensitivity issues
#     text = text.lower()
#     # Compare original string with its reverse
#     if text == text[::-1]:
#         return "Palindrome"
#     else:
#         return "Not a Palindrome"

# # Sample Input
# print(is_palindrome("racecar")) # Output: Palindrome

#Count Vowels and Consonants
# def count_vowels_consonants(text):
#     vowels = "aeiou"
#     v_count = 0
#     c_count = 0
    
#     for char in text.lower():
#         if char.isalpha(): # Ensure it's a letter, not a space/number
#             if char in vowels:
#                 v_count += 1
#             else:
#                 c_count += 1
                
#     return f"Vowels: {v_count}, Consonants: {c_count}"

# # Sample Input
# print(count_vowels_consonants("hello")) # Output: Vowels: 2, Consonants: 3

# Rearrange Positive and Negative Numbers
# def rearrange_alternating(arr):
#     pos = [x for x in arr if x >= 0]
#     neg = [x for x in arr if x < 0]
    
#     result = []
#     i = j = 0
#     # Alternately pick from pos and neg lists
#     while i < len(pos) and j < len(neg):
#         result.append(neg[j])
#         result.append(pos[i])
#         i += 1
#         j += 1
    
#     # Append any leftovers if lists are uneven
#     result.extend(neg[j:])
#     result.extend(pos[i:])
#     return result

# Sample Input: [-1, 2, -3, 4, 5, -6]
# print(rearrange_alternating([-1, 2, -3, 4, 5, -6])) 
# Output: [-1, 2, -3, 4, -6, 5]

# Find the Majority Element
# def find_majority(nums):
#     candidate = None
#     count = 0
    
#     # Phase 1: Find a candidate
#     for num in nums:
#         if count == 0:
#             candidate = num
#         count += (1 if num == candidate else -1)
        
#     return f"Majority Element: {candidate}"

# Sample Input: [3, 3, 4, 2, 4, 4, 2, 4, 4]
# print(find_majority([3, 3, 4, 2, 4, 4, 2, 4, 4])) 
# Output: Majority Element: 4

# Product of Array Except Self
# def product_except_self(nums):
#     n = len(nums)
#     res = [1] * n
    
#     # Left pass: Calculate products of elements to the left
#     left_product = 1
#     for i in range(n):
#         res[i] = left_product
#         left_product *= nums[i]
        
#     # Right pass: Multiply by products of elements to the right
#     right_product = 1
#     for i in range(n - 1, -1, -1):
#         res[i] *= right_product
#         right_product *= nums[i]
        
#     return res

# # Sample Input: [1, 2, 3, 4]
# # Expected Output: [24, 12, 8, 6]
# print(product_except_self([1, 2, 3, 4]))

# #Find Maximum and Minimum Elements
# def find_max_min(arr):
#     if not arr:
#         return None
    
#     # Initialize with the first element
#     maximum = minimum = arr[0]
    
#     for num in arr:
#         if num > maximum:
#             maximum = num
#         if num < minimum:
#             minimum = num
            
#     return f"Maximum: {maximum}, Minimum: {minimum}"

# # Sample Input: [5, 3, 9, 2, 8]
# print(find_max_min([5, 3, 9, 2, 8])) # Output: Maximum: 9, Minimum: 2

#Find the Second Largest Element
def second_largest(arr):
    first = second = float('-inf') # Initialize to negative infinity
    
    for num in arr:
        if num > first:
            # Current becomes second, new becomes first
            second = first
            first = num
        elif num > second and num != first:
            # New number is between first and second
            second = num
            
    return f"Second Largest: {second}"

# Sample Input: [7, 3, 9, 2, 8]
print(second_largest([7, 3, 9, 2, 8])) # Output: Second Largest: 8

# Remove Duplicates from Unsorted Array
def remove_duplicates(arr):
    seen = set()
    result = []
    
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
            
    return result

# Sample Input: [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5])) # Output: [1, 2, 3, 4, 5]

