"""Sunland operates two types of transport services for its annual Summer Festival: Buses and Shuttles, where a bus can carry up to 80 people and a shuttle can carry up to 8 people.

There are N people eager to visit the festival, and the city government needs to transport all of them from various starting points to the festival grounds in the most cost-efficient way possible. You know that the fuel price in Sunland is 75 coins per litre, and:

Each Bus requires P litres of fuel to complete the trip. Each Shuttle requires Q litres of fuel for the same trip.

Your task

Find and return an integer value representing the minimum fuel cost to transport all N people to the festival.

Input Format

An integer value N representing the total number of people.
An integer value P representing the litres of fuel used by one bus.
An integer value Q representing the litres of fuel used by one shuttle.
Constraints

NA

Output Format

Return an integer value representing the minimum fuel cost required to transport all people to the festival grounds.

Sample Input 0

240
50
8
Sample Output 0

11250
Explanation 0

Here, there are 240 people, P = 50, and Q = 8.

To transport 240 people, we can use 3 Buses (since each bus carries 80 people).

Total cost:

3 × 50 × 75 = 11250 coins

No shuttles are needed in this case.

Thus, 11250 is returned as the output.

Sample Input 1

95
60
10
Sample Output 1

6000
Explanation 1

Here, there are 95 people, P = 60, and Q = 10.

We can transport 80 people in the following manner:

80 people will be transported using 1 bus, which will cost:

1 × 60 × 75 = 4500 coins

The remaining 15 people can be transported using 2 shuttles, costing:

2 × 10 × 75 = 1500 coins

Thus, the total cost will be:

4500 + 1500 = 6000 coins

Hence, 6000 is returned as output."""
N = int(input())
P = int(input())
Q = int(input())

total_buses = N//80
remaining_people = N%80

total_shuttles = (remaining_people+7)//8

total_fuel = (total_buses*P)+(total_shuttles*Q)

total_cost = total_fuel*75

print(total_cost)