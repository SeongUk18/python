import pandas as pd
import numpy as np

# 데이터 수집
data = {
    'name': ['Alice', 'Bob', 'Charlie', None],
    'age': [25, 30, 35, np.nan],
    'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', None]
}

df = pd.DataFrame(data)

# 데이터 정리 및 클렌징
df.dropna(subset=['name', 'email'], inplace=True)  # name과 email에 결측값이 있는 행 제거
df['age'].fillna(df['age'].mean(), inplace=True)  # age의 결측값을 평균으로 대체

# 데이터 변환
df['age'] = df['age'].astype(int)  # age를 정수형으로 변환

# 데이터 필터링 및 선택
filtered_df = df[df['age'] > 30]  # age가 30보다 큰 데이터만 선택

# 데이터 요약 및 집계
summary = df.groupby('age').size()  # age별로 그룹화하여 개수 세기

print("Filtered DataFrame:")
print(filtered_df)
print("\nSummary by Age:")
print(summary)

'''
Filtered DataFrame:
      name  age              email
2  Charlie   35  charlie@example.com

Summary by Age:
age
25    1
30    1
35    1
dtype: int64
'''