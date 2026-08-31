import math


def main():
    # Accept 4 inputs sequentially as specified in the problem statement
    N = int(input("number of pencils available: ").strip())  # Total pencils available
    M = int(input("number of erasers available: ").strip())  # Total erasers available
    P = int(input("number of pencils to buy: ").strip())  # Pencils to buy
    E = int(input("number of erasers to buy: ").strip())  # Erasers to buy

    # Check if the requested items exceed available inventory
    if P > N or E > M or P < 0 or E < 0:
        print(0)
        return

    # Calculate combinations using math.comb (available in Python 3.8+)
    ways_pencils = math.comb(N, P)
    ways_erasers = math.comb(M, E)

    # Total ways is the product of individual choices
    total_ways = ways_pencils * ways_erasers

    print(total_ways)


if __name__ == '__main__':
    main()
