#jofi tri fathan afiq
#2510457

def fibonacci(n):
    deret = [0, 1]
    for i in range(2, n):
        next = deret[i-1] + deret [i-2]
        deret.append(next)

    return deret[:n]

print(fibonacci(999))
