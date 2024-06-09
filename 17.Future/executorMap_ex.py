import concurrent.futures


def compute_square(n):
    return n * n


numbers = [1, 2, 3, 4, 5]

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(compute_square, numbers)

    for result in results:
        print(result)

'''
1
4
9
16
25
'''