def is_factorial(n):
    i = f = 1
    while f < n:
        i += 1
        f *= i
    return f == n


string = input("Enter a string: ")
total_a = 0
for i in string:
    if i == 'a':
        total_a += 1
if is_factorial(total_a):
    print("'{}' this string is acceptable by this context free language.".format(string))
else:
    print("'{}' this string is not accepted by this context free language.".format(string))
