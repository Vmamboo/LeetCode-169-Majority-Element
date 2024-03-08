def majorityElement(nums) -> int:
    elements = {}
    
    # Iterate through the input list 'nums'
    for x in nums:
        # Check if the element 'x' is already in the dictionary
        if x in elements.keys():
            # If yes, increment the count for that element
            elements[x] += 1
        else:
            # If not, add the element to the dictionary with a count of 1
            elements[x] = 1
    
    # Iterate through the keys in the dictionary
    for key in elements.keys():
        # Check if the count of the current element is equal to the maximum count in the dictionary
        if elements[key] == max(list(elements.values())):
            return key

# Example usage
nums_list = [1, 2, 2, 3, 2, 4, 2, 2, 5]

result = majorityElement(nums_list)

if result is not None:
    print(f'The majority element is: {result}')
else:
    print('No majority element found in the list.')
