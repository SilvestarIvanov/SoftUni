
nums = ["even" if num % 2 == 0 else "odd" for num in range(1, 11)]

# list comprehension to make a list 1 to 10
# nums = [num for num in range(1, 11)]

# for num in range(1, 11):
#   nums.append(num)

# how to append even number with for:
# for num in range(1, 11):
#   if num % 2 == 0:
#       nums.append(num)

# how to append even number wit list comprehension:
# nums = [num for num in range(1, 11) if num % 2 == 0]

# list comprehension to make a list of strings to list of integers

nums_as_strings = ["1", "2", "3", "4", "5"]
print(nums_as_strings)

nums = [int(elements) for elements in nums_as_strings]
# for elements in nums_as_strings:
#   nums.append((int(elements))

print(nums)