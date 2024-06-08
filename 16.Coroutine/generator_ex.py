gen_exp = (x * x for x in range(10))

for num in gen_exp:
    print(num)


def read_large_file(file_path):
    with open(file_path, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            yield line


for line in read_large_file('large_file.txt'):
    print(line)

    