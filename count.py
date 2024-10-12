# Python3 program for the above approach

# Function to find longest possible
# subsequence of s beginning with x and y 
def solve(s, x, y):

	res = 0

	# Iterate over the string
	for c in s:
		if(ord(c) - ord('0') == x):

			# Increment count
			res += 1

			# Swap the positions
			x, y = y, x

	if(x != y and res % 2 == 1):
		res -= 1

	# Return the result
	return res

# Function that finds all the
# possible pairs
def find_min(s):

	count = 0
	for i in range(10):
		for j in range(10):

			# Update count
			count = max(count, solve(s, i, j))

	# Return the answer 
	return count

# Driver Code

# Given string s
s = "100120013"

# Find the size of the string
n = len(s)

# Function call
answer = find_min(s)

# This value is the count of
# minimum element to be removed
print(n - answer)

# This code is contributed by Shivam Singh
