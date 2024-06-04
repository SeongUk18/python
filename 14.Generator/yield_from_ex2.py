def subgenerator():
    try:
        yield 1
        yield 2
    except ValueError:
        yield "ValueError caught"


def delegating_generator():
    yield from subgenerator()


# Usage
gen = delegating_generator()
print(next(gen))  # 1
print(next(gen))  # 2
gen.throw(ValueError)  # "ValueError caught"

'''
1
2
ValueError caught
'''