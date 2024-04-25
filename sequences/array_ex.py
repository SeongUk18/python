import array

# 실수(float) 타입의 배열 생성
float_array = array.array('f', [1.0, 1.5, 2.0, 2.5])

# 배열 요소 출력
for element in float_array:
    print(element)

# 배열 요소에 접근
print(float_array[1])  # 출력: 1.5

# 배열 요소 변경
float_array[1] = 1.6
print(float_array[1])  # 출력: 1.6