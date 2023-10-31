def solution(requests, totalslots):
    memory = [0] * totalslots
    result = []

    def find_next_free(start):
        count = 0
        for i in range(start, start + totalslots):
            index = i % totalslots
            if memory[index] == 0:
                count += 1
                if count == int(request[2]):
                    return i - int(request[2]) + 1
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