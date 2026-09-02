"""You are a marketing analyst tasked with identifying products to feature in a promotional campaign. Each product has a unique identifier M, and you use a metric called the "Star Sum" to evaluate these products.

The Star Sum of an identifier M is the sum of all non-empty prefixes of M.

For example, the star sum of 5043 is:

5 + 50 + 504 + 5043 = 5602.

Given an integer N, your task is to find and return the count of values of M, such that M ≤ N and the star sum of M is greater than N.

Input Format

An integer value N

Constraints

NA

Output Format

Return an integer value representing the count of values M, such that M ≤ N and the star sum of M is greater than N.

Sample Input 0

112
Sample Output 0

11
Explanation 0

For N = 112 calculate the star sum for integers up to 112. The star sums for values from 100 to 112 are greater than 112. There are 11 such values

Star sum of 100 = 1 + 10 + 100 = 111

Star sum of 101 = 1 + 10 + 101 = 112

Star sum of 102 = 1 + 10 + 102 = 113

Star sum of 103 = 1 + 10 + 103 = 114

Star sum of 104 = 1 + 10 + 104 = 115

Star sum of 105 = 1 + 10 + 105 = 116

Star sum of 106 = 1 + 10 + 106 = 117

Star sum of 107 = 1 + 10 + 107 = 118

Star sum of 108 = 1 + 10 + 108 = 119

Star sum of 109 = 1 + 10 + 109 = 120

Star sum of 110 = 1 + 11 + 110 = 122

Star sum of 111 = 1 + 11 + 111 = 123

Star sum of 112 = 1 + 11 + 112 = 124

There are 11 values of M which are less than or equal to 112 and whose star sum is greater than 112. Hence, 11 is returned as output.

Sample Input 1

5
Sample Output 1

0
Explanation 1

For N = 5, calculate the star sum for integers up to 5.

Star sum of 1 = 1

Star sum of 2 = 2

Star sum of 3 = 3

Star sum of 4 = 4

Star sum of 5 = 5

For N = 5, the star sums for all integers from 1 to 5 are not greater than 5. Hence 0 is returned as the output."""
N = int(input())

count = 0

for M in range(1, N + 1):

    s = str(M)
    prefix = 0
    star_sum = 0

    for digit in s:
        prefix = prefix * 10 + int(digit)
        star_sum += prefix

    if star_sum > N:
        count += 1

print(count)