squares_even = [x**2 for x in range(10) if x % 2 == 0]
print(squares_even) # [0, 4, 16, 36, 64]

squares_gen = (x**2 for x in range(10))
for value in squares_gen:
    print(value) # 0, 1, 4, 9, 16, 25, 36, 49, 64, 81