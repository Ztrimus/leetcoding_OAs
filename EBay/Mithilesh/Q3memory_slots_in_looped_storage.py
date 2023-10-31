def solution(requests, totalslots):
    memory = [0] * totalslots
    result = []

    def find_next_free(start):
        count = 0
        for i in range(start, start + totalslots):
            index = i % totalslots
            if count == 0:
                a = index
            if memory[index] == 0:
                count += 1
                if count == int(b):
                    return a
            else:
                count = 0
        return -1

    for request in requests:
        ty, a, b = request
        if ty == "store":
            startIndex = int(a)
            allocated = find_next_free(startIndex)
            
            if allocated == -1:
                result.append(-1)
            else:
                for i in range(allocated, allocated + int(b)):
                    memory[i % totalslots] = 1
                result.append(allocated)
        elif ty == "free":
            startIndex = int(a)
            for i in range(startIndex, startIndex + int(b)):
                memory[i % totalslots] = 0
            result.append(int(b))

    return result
totalslots = 15
requests = [ ["store", "0", "6"],
            ["store", "11", "3"],
            ["free", "0", "3"],
            ["store", "10", "3"],
            ["store", "6", "6"]]
print(solution(requests, totalslots))