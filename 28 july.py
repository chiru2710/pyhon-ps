# 1.wap to find pNumbers in certain range?
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Prime numbers between {start} and {end} are:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")
# 2.wap to find pNumbers in list? And  create new list?
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

original_list = [3, 4, 7, 10, 13, 17, 20, 23]
prime_list = [num for num in original_list if is_prime(num)]

print("Original list:", original_list)
print("Prime numbers in list:", prime_list)
