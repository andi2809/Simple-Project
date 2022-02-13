def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


as_much = int(input("Ingin menampilkan bilangan fibbonaci sebanyak?"))

print("Bilangan fibonacci sebanyak: ", as_much)
seq = fibonacci_numbers(as_much)
for numbers in seq:
    print(numbers)

# def square(nums):
#     for num in nums:
#         yield num**2
#
# print(sum(square(fibonacci_numbers(10))))
