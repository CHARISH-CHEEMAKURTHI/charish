# t=int(input())
# for i in range(t):
#     nm=input().split()
#     c=0
#     a=True
#     ab=[]
#     while a:
#         c+=1
#         if c <= int(nm[0]):
#             ab=input().split()
#         else:
#             a=False
import sys


def solve():
    """
    Solves a single test case for the Farmer John Pacer Test problem.
    """
    try:
        n, m = map(int, sys.stdin.readline().split())
        reqs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    except (IOError, ValueError):
        return

    # Add the starting point (time 0, side 0) to the list of requirements
    # This makes it easier to process all intervals in a single loop.
    checkpoints = [[0, 0]] + reqs

    total_score = 0

    # Process intervals between checkpoints
    # We identify "cycles" (runs of checkpoints on the same side)
    # and "transitions" (when the side changes).
    i = 0
    while i < len(checkpoints):
        # Find the start of the current segment
        start_a, start_b = checkpoints[i]

        # Find the end of the current cycle (all subsequent points on the same side)
        j = i + 1
        while j < len(checkpoints) and checkpoints[j][1] == start_b:
            j += 1

        # The cycle is from checkpoint i to j-1
        end_of_cycle_a, end_of_cycle_b = checkpoints[j - 1]

        # The score within this cycle is simply the duration.
        # FJ can run back and forth, hitting all intermediate checkpoints.
        cycle_score = end_of_cycle_a - start_a
        total_score += cycle_score

        # Now, handle the transition to the next different-sided checkpoint, if it exists
        if j < len(checkpoints):
            next_a, next_b = checkpoints[j]

            # This is the transition from the end of our cycle to the next point
            # Interval: (end_of_cycle_a, end_of_cycle_b) -> (next_a, next_b)
            delta_t = next_a - end_of_cycle_a

            # An elegant parity check: (time + side) must have the same
            # parity at the start and end of an interval to run every minute.
            if (end_of_cycle_a + end_of_cycle_b) % 2 == (next_a + next_b) % 2:
                total_score += delta_t
            else:
                total_score += delta_t - 1

        # Move index to the start of the next segment
        i = j

    # Add points from the last requirement to the end of the test
    last_req_time = checkpoints[-1][0]
    total_score += (m - last_req_time)

    print(total_score)


def main():
    """
    Main function to handle multiple test cases.
    """
    try:
        t = int(sys.stdin.readline())
        for _ in range(t):
            solve()
    except (IOError, ValueError):
        return


if __name__ == "__main__":
    main()