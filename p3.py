def add_difference(n1, n2):
    total = 0
    if n2 < n1:
        return total
    else:
        for i in range(n1, n2 + 1):
            total += i
        return total


my_number = add_difference(9, 11)
print(my_number)
