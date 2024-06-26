import numpy as np

# 4x4 배열 생성
arr = np.array([[ 1,  2,  3,  4],
                [ 5,  6,  7,  8],
                [ 9, 10, 11, 12],
                [13, 14, 15, 16]])

# 배열의 첫 번째 및 두 번째 행과, 두 번째 및 세 번째 열을 슬라이싱
sub_array = arr[0:2, 1:3]
print(sub_array)
# [[2 3]
# [6 7]]

# 3x4x5 배열 생성
arr = np.random.randint(1, 100, (3, 4, 5))

# 첫 번째 차원의 첫 번째 요소, 중간 차원 전체, 마지막 차원의 첫 번째 요소 슬라이싱
# 3차원 배열의 첫 번째 "페이지"에서 각 행의 첫 번째 열을 선택한다. ...는 배열의 모든 행을 포함하도록 한다.
slice_result = arr[0, ..., 0]
print(slice_result)