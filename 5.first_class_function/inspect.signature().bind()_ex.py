import inspect

def sample_function(a, b, c=3, *args, d, e=5, **kwargs):
    pass

# 함수의 시그니처 가져오기
signature = inspect.signature(sample_function)

# 시그니처에 인수 바인딩 시도
bound_args = signature.bind(1, 2, 3, d=4)

# 바인딩 결과 출력
print("Arguments:") # Arguments:
for name, value in bound_args.arguments.items():
    print(f"{name}: {value}")
    # a: 1
		# b: 2
		# c: 3
		# d: 4

# 바인딩된 인수로 함수 호출 가능성 확인
sample_function(*bound_args.args, **bound_args.kwargs)