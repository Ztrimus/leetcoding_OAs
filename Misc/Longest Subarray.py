def maxLength(a, k):
    n = len(a)
    max_length = 0
    current_sum = 0
    left = 0

    for right in range(n):
        current_sum += a[right]

        while current_sum > k:
            current_sum -= a[left]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

# Input from the user
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
k = int(input())

result = maxLength(a, k)
print("result: ",result)


[]