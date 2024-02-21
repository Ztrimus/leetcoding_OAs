import collections
service_nodes = 5
service_from = [1,2,3,4]
service_to = [2,3,4,5]
k = 2
current_values = [[1,3],[5,3]]


# service_nodes = 4
# service_from = [1,2,2]
# service_to = [2,3,4]
# k = 3
# current_values = [[1,3],[2,4],[3,3]]

# service_nodes = 3
# service_from = [1,1]
# service_to = [2,3]
# k = 2
# current_values = [[2,4],[3,6]]

adjacency_list = collections.defaultdict(list)


for f, t in zip(service_from, service_to):
    adjacency_list[f].append(t)
    adjacency_list[t].append(f)

answer = [-1] * service_nodes

def find_threads():
    visited = set()
    queue = collections.deque()

    for node, val in current_values:
        answer[node - 1] = val
        queue.append(node)
    print(k)
    while queue:
        current = queue.popleft()

        if current in visited:
            continue

        visited.add(current)

        for neighbor in adjacency_list[current]:
            if answer[neighbor - 1] == -1:
                if answer[current - 1] == 1:
                    answer[neighbor - 1] = answer[current - 1] + 1
                else:
                    answer[neighbor - 1] = answer[current - 1] - 1
            else:
                if abs(answer[current - 1] - answer[neighbor - 1]) != 1:
                    answer[neighbor - 1] = (answer[neighbor - 1] + answer[current - 1]) // 2 + 1

            if neighbor not in visited:
                queue.append(neighbor)

find_threads()

print(answer)
