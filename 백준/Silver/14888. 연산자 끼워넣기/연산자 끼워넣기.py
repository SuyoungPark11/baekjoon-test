n = int(input())
numbers = list(map(int, input().split()))
add, subtract, multiply, divide = map(int, input().split())

max_value = float('-inf')
min_value = float('inf')

def backtrack(idx, result, add, subtract, multiply, divide):
    global max_value, min_value

    if idx == n:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return

    if add > 0:
        backtrack(idx + 1, result + numbers[idx], add - 1, subtract, multiply, divide)

    if subtract > 0:
        backtrack(idx + 1, result - numbers[idx], add, subtract - 1, multiply, divide)

    if multiply > 0:
        backtrack(idx + 1, result * numbers[idx], add, subtract, multiply - 1, divide)

    if divide > 0:
        if result < 0:
            backtrack(idx + 1, -(-result // numbers[idx]), add, subtract, multiply, divide - 1)
        else:
            backtrack(idx + 1, result // numbers[idx], add, subtract, multiply, divide - 1)

backtrack(1, numbers[0], add, subtract, multiply, divide)

print(max_value)
print(min_value)