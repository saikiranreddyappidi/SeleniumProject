def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def pumping_lemma_proof(s):
    # set the pumping length to p = |s|
    p = len(s)

    # find a decomposition of s into u, v, x, y, z
    for i in range(2, p):
        if s[i] == '!':
            u = s[:i + 1]
            v = s[i + 1:i + 3]
            x = s[i + 3:]
            break

    # check that the decomposition satisfies the pumping lemma conditions
    if len(v + x) <= p and len(v) > 0:
        # set y and z to be the remaining parts of x
        y = x[:p - len(v) - len(u)]
        z = x[p - len(v) - len(u):]

        # check that uv^ixy^iz is not in L for all i >= 0
        for i in range(0, p):
            n = (len(u + (v * i) + x + (y * i) + z) - 1) // 2
            if u + (v * i) + x + (y * i) + z != 'a' * n + str(factorial(n)):
                return False
        return True
    else:
        return False


# take input from the user
s = input("Enter a string in the language L: ")

# test the pumping lemma proof on the input string
if pumping_lemma_proof(s):
    print(s, "is in L")
else:
    print(s, "is not in L")
