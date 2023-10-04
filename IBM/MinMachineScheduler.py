import heapq

def getMinMachines(start, end):
    if not start or not end or len(start) != len(end):
        return 0

    n = len(start)
    finish_times = []  # Min heap to store finish times of classrooms

    # Sort intervals by starting time
    sorted_tasks = sorted(zip(start, end), key=lambda x: x[0])

    for j in range(n):
        scheduled = False

        # Check if the lecture j is compatible with some classroom
        if finish_times and sorted_tasks[j][0] > finish_times[0]:
            # Schedule lecture j in an existing classroom
            heapq.heappop(finish_times)
            heapq.heappush(finish_times, sorted_tasks[j][1])
            scheduled = True

        if not scheduled:
            # Allocate a new classroom
            heapq.heappush(finish_times, sorted_tasks[j][1])
    return len(finish_times)  # Minimum number of machines needed

# Example usage
start = [1, 8, 3, 9, 6]
end = [7, 9, 6, 14, 71]
print(getMinMachines(start, end))  # Output: 3

# Example usage
start = [2,2,2,2]
end = [5,5,5,5]

print(getMinMachines(start, end))  # Output: 3

start = [2,1,5,5,8]
end = [5,3,8,6,12]

print(getMinMachines(start, end))  # Output: 3
