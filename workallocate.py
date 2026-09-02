"""In a busy software company, the development team is working on multiple tasks, each with different levels of difficulty. As the project manager, your responsibility is to ensure a fair distribution of workload among the developers. To achieve this, you need to rearrange the tasks in pairs in such a way that the maximum sum of difficulties in any pair is minimized.

You are given an integer array representing the difficulty of N tasks. Your task is to find and return an integer value representing the minimum value of maximum combined difficulty that can be achieved by rearranging the tasks.

Note

N is always even.

Input Format

An integer N, representing the number of tasks.
An integer array representing the difficulty levels of the tasks.
Constraints

NA

Output Format

Return an integer value representing the maximum combined difficulty that can be achieved by rearranging the tasks.

Sample Input 0

6
3 5 2 3 8 7
Sample Output 0

10
Explanation 0

Here, there are 6 tasks and the difficulty levels are {3, 5, 2, 3, 8, 7}. We can pair the tasks in the following maner:

Pair 1: (2, 8) where the combined difficulty is 10

Pair 2: (3, 7) where the combined difficulty is 10

Pair 3: (3, 5) where the combined difficulty is 8.

The maximum combined difficulty is 10, which maximum of the minimum possible. Hence 10 is returned as the output.

Sample Input 1

4
1 6 2 5
Sample Output 1

7
Explanation 1

Here, there are 4 tasks, and the difficulty levels are {1, 6, 2, 5}. We can pair the tasks in the following manner.

Pair 1: (1, 6) where the combined difficulty is 7

Pair 2: (2, 5) where the combined difficulty is 7

The maximum combined difficulty is 7, which maximum of the minimum possible. Hence 7 is returned as the output."""
def min_max_pair_sum(n, difficulties):
    difficulties.sort()
    max_sum = 0
    for i in range(n // 2):
        pair_sum = difficulties[i] + difficulties[n - 1 - i]
        max_sum = max(max_sum, pair_sum)
    return max_sum

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(min_max_pair_sum(n, arr))