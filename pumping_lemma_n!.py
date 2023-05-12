# pumping lemma
# Conditions
# 1. |vxy| <= p
# 2. |vy| > 0
# 3. uv^ixy^iz is in L for all i >= 0
# L = {a^n! | n >= 0}

# divide the string into 5 equal parts
def divide(string):
    k = len(string) // 5
    u = string[:k]
    v = string[k:2 * k]
    x = string[2 * k:3 * k]
    y = string[3 * k:4 * k]
    z = string[4 * k:]
    return [u, v, x, y, z]


def print_condition(k, boolean):
    if boolean:
        print("Condition {} is satisfied".format(k))
    else:
        print("Condition {} is not satisfied".format(k))
        print("String is not in L\nSo given language is not a CFL through contradiction by pumping lemma")
        exit()


def is_factorial(n):
    i = f = 1
    while f < n:
        i += 1
        f *= i
    return f == n


def check_1(v, x, y, pumpingLength):
    if len(v + x + y) <= pumpingLength:
        print_condition(1, True)
    else:
        print_condition(1, False)


def check_2(v, x, y):
    if len(v + y) > 0:
        print_condition(2, True)
    else:
        print_condition(2, False)


def check_3(u, v, x, y, z):
    for i in range(1, 10):
        string = u + (v * i) + x + (y * i) + z
        print("Checking if '{}' is in L for values(u='{}',v='{}',x='{}',y='{}',z='{}' and i={})".format(string, u, v*i,
                                                                                                        x, y*i, z, i))
        if is_factorial(len(string)):
            print("'{}' is in L".format(string))
        else:
            print("'{}' is not in L".format(string))
            print_condition(3, False)


def print_line():
    print("--------------------------------------------------\n")


if __name__ == '__main__':
    string = input("Enter a string: ")
    pumpingLength = int(input("Enter a value for p: "))
    print_line()
    if len(string) > pumpingLength:
        print("String length is greater than p")
        print("String is not in L")
        exit()
    else:
        print("String length is less than p")
    print_line()
    parts = divide(string)
    u, v, x, y, z = parts
    print("Divided the string '{}' into {} parts".format(string, 5))
    print("Parts: {}".format(parts))
    print_line()
    print("Checking the conditions with the string '{}'".format(string))
    print("Checking condition 1")
    check_1(v, x, y, pumpingLength)
    print_line()
    print("Checking condition 2")
    check_2(v, x, y)
    print_line()
    print("Checking condition 3")
    check_3(u, v, x, y, z)
    print("All conditions are satisfied")
    print("String is in L. So given language is a CFL")
